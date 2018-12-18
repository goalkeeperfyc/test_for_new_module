# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:24:30 2018

It takes 8.5 hours to caculate 9088171 lines in short-video-weekly/daily-url-2018_w23_s1
when setting threads_num = 10 in actual program execution, see detail in log file
on server 192.168.17.11 file
/home/hanye/project_data/Python/Projects/proj-short-videos/write-data-into-es/log/
cal_weekly_net_inc_for_daily-url-2018_w23_s1_on_2018-07-04T18-38-35.987666_log

A rough estimate earilier shows about 50 hours time expense in single thread on
the same data set.

@author: hanye
"""

import datetime
import re
import sys
import threading
import copy
import logging
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from func_find_week_num import find_week_belongs_to
from func_find_week_num import day_by_week_info
from func_general_bulk_write import bulk_write_short_video
from func_cal_doc_id import cal_doc_id


es = Elasticsearch(hosts='192.168.17.11', port=9200)

def find_error_from_bulk_resp(resp):
    err_msg_Lst = []
    if resp is not None:
        if resp['errors'] is True:
            for line in resp['items']:
                if line['index']['status'] == 400:
                    err_msg = line['index']['error']
                    err_id = line['index']['_id']
                    err_msg_Lst.append({err_id: err_msg})
            return err_msg_Lst


def parse_week_param(doc_type_weekly):
    try:
        week_year = re.findall('[0-9]{4}', doc_type_weekly)[0]
        week_no_raw_str = re.findall('_w[0-9]{2}_', doc_type_weekly)[0]
        week_no = week_no_raw_str[2:4]
        week_day_start_raw_str = re.findall('_s[1-7]{1}', doc_type_weekly)[0]
        week_day_start = week_day_start_raw_str[2:3]
        return {'week_year': int(week_year),
                'week_no': int(week_no),
                'week_day_start': int(week_day_start)}
    except:
        return None


def find_value_after_fetch_day(platform, url, fetch_dayD,
                               fetch_time_upper_bdrT,
                               data_dict,
                               index='short-video-production',
                               doc_type='daily-url'):
    fetch_day_str = fetch_dayD.isoformat()
    video_id_bare = cal_doc_id(platform, url, fetch_day_str=fetch_day_str,
                               data_dict=data_dict,
                               doc_id_type='bare')
    fetch_time_start_ts = int(datetime.datetime(fetch_dayD.year,
                                                fetch_dayD.month,
                                                fetch_dayD.day).timestamp()*1e3)
    fetch_time_end_ts = int(fetch_time_upper_bdrT.timestamp()*1e3)
    if platform in ['toutiao', 'new_tudou']:
        search_bd = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"platform.keyword": platform}},
                        {"range": {"fetch_time": {"gte": fetch_time_start_ts,
                                                  "lt": fetch_time_end_ts}}}
                    ],
                    "must": [
                        {"match_phrase": {"url": video_id_bare}}
                    ]
                }
            },
            "sort": [
                {"fetch_time": {"order": "asc"}}
                ]
        }
    else:
        search_bd = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"platform.keyword": platform}},
                        {"range": {"fetch_time": {"gte": fetch_time_start_ts,
                                                  "lt": fetch_time_end_ts}}},
                        {"term": {"url.keyword": url}}
                    ],
                }
            },
            "sort": [
                {"fetch_time": {"order": "asc"}}
                ]
        }
    try:
        search_pre_resp = es.search(index=index, doc_type=doc_type,
                                    body=search_bd, size=1,
                                    request_timeout=100)
        hits_total = search_pre_resp['hits']['total']
        if hits_total > 0:
            pre_dict = search_pre_resp['hits']['hits'][0]['_source']
            doc_id = search_pre_resp['hits']['hits'][0]['_id']
            value_dict = {'play_count': pre_dict['play_count'],
                          'fetch_time': pre_dict['fetch_time'],
                          'doc_id': doc_id}
            if 'favorite_count' in pre_dict:
                value_dict.update({'favorite_count': pre_dict['favorite_count']})
            else:
                value_dict.update({'favorite_count': 0,})
            if 'comment_count' in pre_dict:
                value_dict.update({'comment_count': pre_dict['comment_count'],})
            else:
                value_dict.update({'comment_count': 0,})
            return value_dict
        else:
            return None
    except:
        return None


def form_sub_value_result(weekly_cal_base, pre_week_value, curr_data_dict):
    WNI_hist_data_id = pre_week_value['doc_id']
    try:
        weekly_net_inc_play_count = (curr_data_dict['play_count']
                                     - pre_week_value['play_count'])
    except:
        return None
    else:
        if 'favorite_count' in curr_data_dict and 'favorite_count' in pre_week_value:
            weekly_net_inc_favorite_count = (curr_data_dict['favorite_count']
                                             - pre_week_value['favorite_count'])
        else:
            weekly_net_inc_favorite_count = 0
        if 'comment_count' in curr_data_dict and 'comment_count' in pre_week_value:
            weekly_net_inc_comment_count = (curr_data_dict['comment_count']
                                            - pre_week_value['comment_count'])
        else:
            weekly_net_inc_comment_count = 0
        sub_result = {'weekly_cal_base': weekly_cal_base,
                      'WNI_hist_data_id': WNI_hist_data_id,
                      'weekly_net_inc_play_count': weekly_net_inc_play_count,
                      'weekly_net_inc_favorite_count': weekly_net_inc_favorite_count,
                      'weekly_net_inc_comment_count': weekly_net_inc_comment_count}
        return sub_result


def sub_pre_week(curr_doc_type_weekly, curr_data_dict):
    url = curr_data_dict['url']
    fetch_day_T = datetime.datetime.fromtimestamp(curr_data_dict['fetch_time']/1e3)
    platform = curr_data_dict['platform']
    seven_days_before = fetch_day_T - datetime.timedelta(days=7)
    week_info = parse_week_param(curr_doc_type_weekly)
    if week_info != None:
        week_day_start = week_info['week_day_start']
        pre_week_year, pre_week_no, pre_weekday = find_week_belongs_to(
            seven_days_before, week_day_start)
        last_day_in_pre_weekD = day_by_week_info(pre_week_year, pre_week_no, 7,
                                                 week_day_start)
        pre_week_value = find_value_after_fetch_day(platform, url,
                                                    last_day_in_pre_weekD,
                                                    fetch_day_T,
                                                    data_dict=curr_data_dict)
        if pre_week_value is not None:
            pre_week_data_fetch_time = pre_week_value['fetch_time']
            try:
                pre_week_data_fetch_timeT = (datetime.datetime
                                             .fromtimestamp(pre_week_data_fetch_time/1e3))
                pre_week_data_fetch_timeD = datetime.date(pre_week_data_fetch_timeT.year,
                                                          pre_week_data_fetch_timeT.month,
                                                          pre_week_data_fetch_timeT.day)
                if pre_week_data_fetch_timeD == last_day_in_pre_weekD:
                    weekly_cal_base = 'historical_complete'
                else:
                    weekly_cal_base = 'historical_uncomplete'
                sub_result = form_sub_value_result(weekly_cal_base,
                                                   pre_week_value,
                                                   curr_data_dict)
            except:
                print('Got exception, probably because of fetch_time ill-formated.')
                return None
        else:
            sub_result = {'weekly_cal_base': 'historical_data_absent'}
        return sub_result
    else:
        return None


def cal_weekly_net_inc(curr_doc_type_weekly, data_dict):
    if 'release_time' in data_dict and 'fetch_time' in data_dict and 'url' in data_dict:
        week_info = parse_week_param(curr_doc_type_weekly)
        first_day_in_weekD = day_by_week_info(week_info['week_year'],
                                              week_info['week_no'], 1,
                                              week_info['week_day_start'])
        first_day_in_weekT = datetime.datetime(first_day_in_weekD.year,
                                               first_day_in_weekD.month,
                                               first_day_in_weekD.day)
        first_day_in_week_ts = int(first_day_in_weekT.timestamp()*1e3)
        try:
            release_time = int(data_dict['release_time'])
        except:
            return None
        if release_time >= first_day_in_week_ts:
            weekly_cal_base = 'accumulate'
            try:
                weekly_net_inc_play_count = data_dict['play_count']
            except:
                pass
            else:
                if 'favorite_count' in data_dict:
                    weekly_net_inc_favorite_count = data_dict['favorite_count']
                else:
                    weekly_net_inc_favorite_count = 0
                if 'comment_count' in data_dict:
                    weekly_net_inc_comment_count = data_dict['comment_count']
                else:
                    weekly_net_inc_comment_count = 0
                sub_result = {'weekly_cal_base': weekly_cal_base,
                              'weekly_net_inc_play_count': weekly_net_inc_play_count,
                              'weekly_net_inc_favorite_count': weekly_net_inc_favorite_count,
                              'weekly_net_inc_comment_count': weekly_net_inc_comment_count}
        else:
            sub_result = sub_pre_week(curr_doc_type_weekly, data_dict)
        return sub_result
    else:
        return None


def cal_and_bulk_write_with_weekly_net_inc(dict_Lst, doc_type_weekly,
                                           logger_name, thread_id,
                                           index_weekly='short-video-weekly',
                                          ):
    function_name = 'cal_and_bulk_write_with_weekly_net_inc'
    # define logger
    loggerName = '%s.cal_and_bulk_write' % logger_name
    loggerii = logging.getLogger(loggerName)

    if dict_Lst != []:
        loggerii.info('[%d] Calculating weekly net increase values one dict by one.'
                      % (thread_id))
        result_Lst = []
        input_list_size = len(dict_Lst)
        none_res_counter = 0
        for line_d in dict_Lst:
            sub_result = cal_weekly_net_inc(doc_type_weekly, line_d)
            if sub_result != None:
                line_d.update(sub_result)
                result_Lst.append(line_d)
            else:
                none_res_counter += 1
        loggerii.info('[%d] Calculate done, with %d/%d None returns, '
                      'get %d effective results.'
                      % (thread_id, none_res_counter, input_list_size,
                         len(result_Lst)))
        if result_Lst != []:
            try:
                bulk_write_resp = bulk_write_short_video(result_Lst, index=index_weekly,
                                                         doc_type=doc_type_weekly,
                                                         doc_id_type='all-time-url',
                                                         client=es)
                result_Lst.clear()
                return bulk_write_resp
            except:
                loggerii.info('[%d] Got exceptions when bulk write, function %s returns None.'
                              % (thread_id, function_name))
                return None
        else:
            loggerii.info('[%d] Got zero effective results, function %s returns None.'
                          % (thread_id, function_name))
            return None
    else:
        loggerii.info('[%d] Empty input data list, function %s returns None.'
                      % (thread_id, function_name))
        return None

def cal_weekly_net_inc_with_doc_type_name(doc_type_name,
                                          logger_name,
                                          thread_id,
                                          search_body=None,
                                          index_weekly='short-video-weekly',
                                         ):
    # define logger
    loggerName = '%s.in_thread' % logger_name
    loggeri = logging.getLogger(loggerName)

    if search_body is None:
        loggeri.info('[%d] Calculate weekly net increase values for doc_type: %s '
                     'in index: %s.' % (thread_id, doc_type_name, index_weekly))
        find_all_bd = {
            "query": {
                "match_all": {}
            }
        }
    else:
        find_all_bd = copy.deepcopy(search_body)

    search_resp = es.search(index=index_weekly, doc_type=doc_type_name,
                            body=find_all_bd, size=0, request_timeout=100)
    total_hits = search_resp['hits']['total']
    if total_hits > 0:
        loggeri.info('[%d] Total hits: %d with search_body: %s'
                     % (thread_id, total_hits, find_all_bd))
        scan_resp = scan(client=es, index=index_weekly, doc_type=doc_type_name,
                         query=find_all_bd, request_timeout=300)
        line_counter = 0
        ori_data_Lst = []
        for line in scan_resp:
            line_counter += 1
            line_d = line['_source']
            ori_data_Lst.append(line_d)
            if line_counter%1000 == 0 or line_counter == total_hits:
                if thread_id is not None:
                    loggeri.info('[%d] Got lines %d/%d [%.2f%%] to calculate weekly net '
                                 'increase values'
                                 % (thread_id, line_counter, total_hits,
                                    line_counter/total_hits*100))
                bulk_resp = cal_and_bulk_write_with_weekly_net_inc(ori_data_Lst,
                                                                   doc_type_name,
                                                                   loggerName,
                                                                   thread_id,
                                                                   index_weekly=index_weekly,
                                                                  )
                err_msg = find_error_from_bulk_resp(bulk_resp)
                if err_msg is not None:
                    loggeri.info('[%d] Error when bulk write: %s '
                                 % (thread_id, err_msg))
                ori_data_Lst.clear()
    else:
        loggeri.info('[%d] Got zero hits, thread exits.'
                     % (thread_id))
    loggeri.info('[%d] Thread exits.' % (thread_id))


def divid_by_release_time(
        doc_type_name, threads_num=5,
        index_weekly='short-video-weekly',
        query_term=None):
    """
    argument query_term must be a sub dict below keyword 'bool'
    in Elasticsearch search body, such as {'filter' : {'range': {...}}},
    or {'must_not': [...]}
    """

    find_all_bd = {
        "query": {
            "match_all": {}
        },
        "size": 0,
        "aggs": {
            "date_distr": {
                "date_histogram": {
                    "field": "release_time",
                    "interval": "day",
                    "time_zone": "Asia/Shanghai"
                }
            }
        }
    }
    # allow to modify query body
    if query_term is not None:
        find_all_bd['query'].pop('match_all', None)
        find_all_bd['query'].update({'bool': {}})
        find_all_bd['query']['bool'].update(query_term)
    else:
        pass
    search_resp = es.search(index=index_weekly, doc_type=doc_type_name,
                            body=find_all_bd, size=0, request_timeout=100)
    total_hits = search_resp['hits']['total']
    data_distr_by_release_time_Lst = search_resp[
        'aggregations']['date_distr']['buckets']
    if data_distr_by_release_time_Lst == []:
        print('Got empty result from aggregations for doc_type_name: %s, %s'
              % (doc_type_name, datetime.datetime.now()))
        return None
    else:
        average_data_num = total_hits // threads_num
        release_time_range_Lst = []
        data_counter_collector = 0
        distr_idx = 0
        for distr_by_release_dict in data_distr_by_release_time_Lst:
            data_num_each_day = distr_by_release_dict['doc_count']
            data_counter_collector += data_num_each_day
            if (data_counter_collector > average_data_num*0.9
                    or distr_idx == len(data_distr_by_release_time_Lst)-1):
                release_time_range_dict = {'start':None, 'end':None,
                                           'end_idx': distr_idx,
                                           'data_num': data_counter_collector}
                release_time_range_Lst.append(release_time_range_dict)
                data_counter_collector = 0
            distr_idx += 1

        # fillup the start timestamp and the end timestamp
        start_side_cache = data_distr_by_release_time_Lst[0]['key']
        for range_seg in release_time_range_Lst:
            if range_seg['end_idx']+1 > len(data_distr_by_release_time_Lst)-1:
                range_seg['end'] = int(data_distr_by_release_time_Lst[range_seg['end_idx']]['key']
                                       + 24*3600*1e3)
            else:
                range_seg['end'] = data_distr_by_release_time_Lst[range_seg['end_idx']+1]['key']
            range_seg['start'] = start_side_cache
            start_side_cache = range_seg['end']

        # in case the splitted range segments are longer or shorter than threads_num
        if len(release_time_range_Lst) != threads_num:
            threads_num = len(release_time_range_Lst)
        print('actually the thread number is: %d'
              % threads_num)
        print('release_time_range_Lst:\n%s'
              % release_time_range_Lst)

        return (threads_num, release_time_range_Lst, total_hits)


def cal_weekly_net_inc_with_doc_type_name_multi_thread(
        doc_type_name, threads_num=5,
        index_weekly='short-video-weekly',
        query_term=None):
    """
    argument query_term must be a sub dict below keyword 'bool'
    in Elasticsearch search body, such as {'filter' : {'range': {...}}},
    or {'must_not': [...]}
    """

    # define logger
    loggerName = 'cal_weekly_net_inc'
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    # create handler
    path = '/home/hanye/project_data/Python/Projects/proj-short-videos/write-data-into-es/log/'
    log_fn = ('cal_weekly_net_inc_for_%s_on_%s_log'
              % (doc_type_name, datetime.datetime.now().isoformat().replace(':', '-')))
    fh = logging.FileHandler(path+log_fn)
    fh.setLevel(logging.INFO)
    # create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add handler to logger
    logger.addHandler(fh)

    logger.info('************ log starts')

    get_divs = divid_by_release_time(doc_type_name, threads_num,
                                     query_term=query_term)
    if get_divs is None:
        logger.info('Find zero data to be calculated, program exits.')
    else:
        threads_num = get_divs[0]
        release_time_range_Lst = get_divs[1]
        total_hits = get_divs[2]
        logger.info('There are %d lines in %s, '
                    'will start %d threads to calculate.'
                    %(total_hits, doc_type_name, threads_num))
        waitfor = []
        for i in range(0, threads_num):
            release_time_ts_start = release_time_range_Lst[i]['start']
            release_time_ts_end = release_time_range_Lst[i]['end']
            search_bd_in_thread = {
                "query": {
                    "bool": {
                        "filter": [
                            {"range": {"release_time": {
                                "gte": release_time_ts_start,
                                "lt": release_time_ts_end}}},
                        ],
                    }
                },
            }
            # allow to modify search body
            if query_term is not None:
                search_bd_in_thread['query']['bool'].update(query_term)
            else:
                pass
            if  release_time_ts_start <= 0:
                release_time_ts_start = 1
            release_time_start = datetime.datetime.fromtimestamp(release_time_ts_start/1e3)
            release_time_end = datetime.datetime.fromtimestamp(release_time_ts_end/1e3)
            logger.info('Starting thread: %d, '
                        'release_time range: [%s, %s)'
                        % (i, release_time_start, release_time_end))
            threadi = threading.Thread(target=cal_weekly_net_inc_with_doc_type_name,
                                       kwargs={'doc_type_name': doc_type_name,
                                               'logger_name': loggerName,
                                               'search_body': search_bd_in_thread,
                                               'thread_id': i,
                                               'index_weekly': index_weekly})
            waitfor.append(threadi)
            threadi.start()
        for td in waitfor:
            td.join()
        logger.info('Main thread exits.')



## test
#if __name__ == '__main__':
#    doc_type_name = 'daily-url-2018_w25_s1'
#    index = 'short-video-weekly'
#    cal_weekly_net_inc_with_doc_type_name_multi_thread(doc_type_name, index_weekly=index)
