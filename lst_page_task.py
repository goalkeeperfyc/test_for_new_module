# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:10:25 2018

@author: fangyucheng
"""

from crawler.crawler_sys.site_crawler import crawler_v_qq

conf_file = '/home/fangyucheng/python_code/crawler/crawler_sys/utils/lst_page_conf.ini'
task_lst = ['http://v.qq.com/x/list/music',
            'http://v.qq.com/x/list/news',
            'http://v.qq.com/x/list/military',
            'http://v.qq.com/x/list/ent',
            'http://v.qq.com/x/list/sports',
            'http://v.qq.com/x/list/games',
            'http://v.qq.com/x/list/fun',
            'http://v.qq.com/x/list/fashion',
            'http://v.qq.com/x/list/life',
            'http://v.qq.com/x/list/baby',
            'http://v.qq.com/x/list/auto', 
            'http://v.qq.com/x/list/tech', 
            'http://v.qq.com/x/list/education',
            'http://v.qq.com/x/list/finance',
            'http://v.qq.com/x/list/house',
            'http://v.qq.com/x/list/travel',
            'http://v.qq.com/x/list/kings']
crawler = crawler_v_qq.Crawler_v_qq()

for task in task_lst:
    crawler = None
    crawler = crawler_v_qq.Crawler_v_qq()
    crawler.run_lst_page_asyncio(lst_page_url=task)