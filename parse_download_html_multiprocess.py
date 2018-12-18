# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:13:01 2018

@author: fangyucheng
"""


from multiprocessing import Pool
from crawler.crawler_sys.site_crawler import crawler_v_qq

crawler = crawler_v_qq.Crawler_v_qq()

para_dic = {"output_to_file": False,
            "filepath": None,
            "output_to_es_raw": True,
            "output_to_es_register": False,
            "es_index": None,
            "doc_type": None}

pool = Pool(processes=8)
for line in range(8):
    pool.apply_async(crawler.parse_video_page_single_process, args=(para_dic,))
pool.close()
pool.join()