# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:23:35 2018

@author: fangyucheng
"""

import time
import requests

headers = {"content-type": "application/x-www-form-urlencoded",
           "store": "1",
           "accept": "*/*",
           "qn-sig": "781F8ABD64529A42BE1D0BF5986D041B",
           "idft": "CE1E8744-7BF9-4FDD-87A5-463C6B9A66E1",
           "idfa": "05571C2D-1C86-4B5B-87EF-E4B4DAF07DDB",
           "appver": "12.0.1_qqnews_5.7.22",
           "qn-rid": "F79EC39E-D132-4694-B1C0-6292E7006EE3",
           "devid": "d605a70a-d084-487e-aaf1-8a057d40ef39",
           "devicetoken": "<f4b49138 3ca95e38 1519836e daefaab6 799b04da c164f7a7 4cb7d999 6e343393>",
           "accept-language": "zh-Hans-CN;q=1, en-CN;q=0.9",
           "referer": "http://inews.qq.com/inews/iphone/",
           "user-agent": "QQNews/5.7.22 (iPhone; iOS 12.0.1; Scale/2.00)",
           "content-length": "2169",
           "accept-encoding": "br, gzip, deflate",
           "cookie": "logintype=2",
           "qqnetwork": "wifi"}

post_dic = {'chlid': 'news_video_top',
            'forward': '2',
            'uid': '6F0D5898-2C3A-46FE-9181-589BC52ED743',
            'adReqData': '{"chid":2,"adtype":0,"pf":"iphone","launch":"0","ext":{"mob":{"mobstr":"Aejy45+NeSZw4VxymYnnIhMV+MEM+6sW9Rkw16FvkWGCz1rsPQflpTnsN+KnArzMwheqHiLErlbOlNWL0SoBI0lJtRh13iyR+LxSv3Y+hJrixm\\/Sxn\\/YhInAhlYioOjQ9cHGSSRmdgaDyqx2dDLZosKp+QSMqr649GGxQ36xbSdjbvZ3MGywBOsVNcf+EZkV+U9Q8LyDPc6PZ56b\\/GLGncf4XcrVFnKlUi+kebsg8DCD\\/nlvTDGSkWOtu33GJ4Ct\\/hfZ1c3UNHw5bRwHRM0L0+6QYANTrPzl2X6hZK3kijlJsub+RvcPNPNQGrhK3e4yYHJmspW19qE5mPgxd5lbwzJ8VQifTrjGeB+cdCcGmEPYBcZwHmxRhEAo7A0bJcSLK5KACWNsKw8I085yoKLCIE40\\/1J+umH8QsTU6K+wLdpjpaI6D3XMa\\/GZiguAcNB7HMSMpBFY6dq1saxz0u+6Ex2n2CwJlY4JYzf2S4r69t8J1WCQInAjIf\\/Io+ZVhXNnNUx3GVir\\/TaffnYpd\\/5ZvqdKtBIWXZFtXOoWC66tNBG\\/D+YAoY8\\/yVAQL7slsS1qbjdDqByVI2DMq299y6yAh0hejMouwaCGK2Q2OCMes5xrghJ1sotO5mSqioK23WbdF9GiQSVqmbE94wzpCwaPCwrEzkgKWHuPxh0UlqUs9QeGe30SHv4OOpqF9QOUeXYJ\\/Xkana90uC32g3LuM6jdPTv07qbyk1tX87pGdnyvjR9BBEhb0dyLUFi\\/Gx8t4T+yHLxt0X9yKsGKCJX1U8AdkTwLlJslIX9Rzqy+Yb1n9sg85KAS5yUsQZqSv9kKRuZpYsfj6LLaI\\/Bet9BUNtGu4hYuZBqKFWp34XegvS4d3M9U"}},"ver":"5.7.22","slot":[{"islocal":0,"orders_info":["67950414,6870997,0,1000,0,110,2","88685632,1266139,1761176905,19,101,110,3","48980066,1934913,3602870493,19,101,110,1"],"recent_rot":["1,2,3"],"refresh_type":0,"loid":"1,13,16,23","channel":"news_video_top"}],"appversion":"181210"}',
            'kankaninfo': '{"gender":1,"lastExp":416,"refresh":0,"scene":2}',
            'channelPosition': '1',
            'rendType': 'kankan',
            'page': '0'}

post_url = ("https://r.inews.qq.com/getQQNewsUnreadList?appver=12.0.1_qqnews_5.7.22"
    "&pagestartfrom=icon&page_type=timeline&apptype=ios"
    "&rtAd=1&imsi=460-01&screen_height=667"
    "&httpRequestUid=21d3cb678d9a"
    "&qn-sig=781F8ABD64529A42BE1D0BF5986D041B"
    "&network_type=wifi"
    "&startTimestamp=1545835451"
    "&store=1"
    "&deviceToken=%3Cf4b49138%203ca95e38%201519836e%20daefaab6%20799b04da%20c164f7a7%204cb7d999%206e343393%3E"
    "&global_info=1%7C1%7C1%7C1%7C1%7C14%7C4%7C1%7C0%7C6%7C1%7C1%7C2%7C2%7C0%7CJ267P000000000%3AJ060P000000000%3AB054P000015802%3AJ054P600000000%7C1421%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C1001%7C0%7C6%7C1%7C1%7C1%7C1%7C1%7C1%7C-1%7C0%7C0%7C0%7C2%7C1%7C1%7C0%7C0%7C2%7C0%7C1%7C0%7C4%7C0%7C0%7C0%7C3%7C0%7C0%7C0%7C0"
    "&globalInfo=1%7C1%7C1%7C1%7C1%7C14%7C4%7C1%7C0%7C6%7C1%7C1%7C2%7C2%7C0%7CJ267P000000000%3AJ060P000000000%3AB054P000015802%3AJ054P600000000%7C1421%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C1001%7C0%7C6%7C1%7C1%7C1%7C1%7C1%7C1%7C-1%7C0%7C0%7C0%7C2%7C1%7C1%7C0%7C0%7C2%7C0%7C1%7C0%7C4%7C0%7C0%7C0%7C3%7C0%7C0%7C0%7C0"
    "&screen_scale=2&activefrom=icon&screen_width=375"
    "&isJailbreak=0"
    "&qn-rid=F79EC39E-D132-4694-B1C0-6292E7006EE3"
    "&qqnews_refpage=QNCommonListController"
    "&omgid=a305486b92cc9e48f90929497de4cb30dfde0010112206"
    "&device_model=iPhone9%2C1&pagestartFrom=icon"
    "&device_appin=6F0D5898-2C3A-46FE-9181-589BC52ED743"
    "&devid=D605A70A-D084-487E-AAF1-8A057D40EF39"
    "&omgbizid=138dc6ef3ae8a24f7c897a9bbde8b9098f210060113210"
    "&idfa=05571C2D-1C86-4B5B-87EF-E4B4DAF07DDB")

get_page = requests.post(post_url, data=post_dic, headers=headers)