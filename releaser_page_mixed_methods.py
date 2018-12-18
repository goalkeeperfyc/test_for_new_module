# -*- coding: utf-8 -*-

"""
Created on Tue Dec 11 15:46:19 2018

@author: fangyucheng
"""

import sys
import argparse
from multiprocessing import Pool
from crawler.crawler_sys.framework.platform_crawler_register import platform_crawler_reg
from crawler_sys.framework.platform_crawler_register import get_crawler
from crawler.crawler_sys.utils.retrieve_releaserUrl_from_es import get_releaserUrls_from_es

parser = argparse.ArgumentParser(description='Specify a platform name.')
parser.add_argument('-p', '--platform', default=[], action='append',
                    help=('Pass platform names, they will be assembled in python list.'))
parser.add_argument('-w', '--output_to_es_raw', default=True, type=str,
                    help=('Write data into es or not, default to True'))
parser.add_argument('-g', '--output_to_es_register', default=True, type=str,
                    help=('Write data into es or not, default to True'))
parser.add_argument('-f', '--frequency', default=None, type=int,
                    help=('choose a frequency to retrieve releaserUrl,'
                          '1 or 3 is legal number, default None also acceptable'))
parser.add_argument('-s', '--processes_num', default=30, type=int,
                    help=('Processes number to be used in multiprocessing'))
parser.add_argument('-n', '--max_page', default=30, type=int,
                    help=('The max page numbers to be scroll for each releaser url,'
                          'must be an int value, default to 30.'))
args = parser.parse_args()

if args.platform != []:
    platforms = args.platform

for platform in platforms:
    if platform not in platform_crawler_reg:
        print("illegal platform name %s" % platform)
        sys.exit(0)

releaser_page_num_max = args.max_page
output_to_es_raw = args.output_to_es_raw
output_to_es_register = args.output_to_es_register

processes_num = args.processes_num
frequency = args.frequency

kwargs_dict = {
   'releaser_page_num_max': releaser_page_num_max,
   'output_to_es_raw': output_to_es_raw,
   'output_to_es_register': output_to_es_register,
}
for platform in platforms:
    releaserUrl_List = get_releaserUrls_from_es(platform, frequency)
    if releaserUrl_List == []:
        print('Get empty releaserUrl_List for platform %s' % platform)
        continue
    Platform_crawler = get_crawler(platform)
    if Platform_crawler != None:
        crawler_instant = Platform_crawler()
        crawler = crawler_instant.releaser_page
    else:
        print('Failed to get crawler for platform %s' % platform)
        continue
    pool = Pool(processes=processes_num)
    for url in releaserUrl_List:
        pool.apply_async(func=crawler, args=(url,), kwds=kwargs_dict)
    pool.close()
    pool.join()
    print('Multiprocessing done for platform %s' % platform)
