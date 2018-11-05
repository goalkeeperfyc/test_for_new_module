# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:30:03 2018

@author: fangyucheng
"""

import time
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

urls = ["http://www.qq.com",
        "http://www.163.com",
        "http://www.sina.com.cn",
        "http://sports.sina.com.cn/nba/",
        "http://news.sina.com.cn/",
        "http://mil.news.sina.com.cn/",
        "http://news.sina.com.cn/society/",
        "http://news.sina.com.cn/world/",
        "http://finance.sina.com.cn/",
        "http://finance.sina.com.cn/stock/",
        "http://finance.sina.com.cn/fund/",
        "http://finance.sina.com.cn/forex/",
        "http://tech.sina.com.cn/",
        "http://mobile.sina.com.cn/",
        "http://tech.sina.com.cn/discovery/",
        "http://zhongce.sina.com.cn/"]

def wget(url):
    print("wget %s..." % url)
    res = requests.get(url)
    return res.headers
 
async def wget_tasks(executor):
    loop = asyncio.get_event_loop()
    bloking_tasks = []
    for url in urls:
        task = loop.run_in_executor(executor, wget, url)
        task.__url = url
        bloking_tasks.append(task)
    complted, pending = await asyncio.wait(bloking_tasks)
    results = {t.__url: t.result() for t in complted}
    for url, result in sorted(results.items(), key=lambda x: x[0]):
        print("wget",url,result)
 
if __name__ == '__main__':
 
    start = time.time()
    executor = ThreadPoolExecutor(max_workers=10)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(wget_tasks(executor))
    end = time.time()
    t = time.time()-start
    print("Asyncio + request + ProcessPoolExecutor cost:", time.time()-start)