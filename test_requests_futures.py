# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:55:47 2018

@author: fangyucheng
"""

import time
import requests
from requests_futures.sessions import FuturesSession

old_sess = requests.Session()
new_sess = FuturesSession()

url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/get?foo=bar'

old_start = time.time()
resp_one = old_sess.get(url1)
resp_two = old_sess.get(url2)
resp3 = old_sess.get(url1)
resp4 = old_sess.get(url2)
resp5 = old_sess.get(url1)
resp6 = old_sess.get(url2)
resp7 = old_sess.get(url1)
resp8 = old_sess.get(url2)
resp9 = old_sess.get(url1)
resp10 = old_sess.get(url2)
old_re1 = resp_one.json()
old_re2 = resp_two.json()
old_re3 = resp3.json()
old_re4 = resp4.json()
old_re5 = resp5.json()
old_re6 = resp6.json()
old_re7 = resp7.json()
old_re8 = resp8.json()
old_re9 = resp9.json()
old_re10 = resp10.json()
old_end = time.time()
old_cost = old_end - old_start

new_start = time.time()
future1 = new_sess.get(url1)
future2 = new_sess.get(url2)
future3 = new_sess.get(url1)
future4 = new_sess.get(url2)
future5 = new_sess.get(url1)
future6 = new_sess.get(url2)
future7 = new_sess.get(url2)
future8 = new_sess.get(url1)
future9 = new_sess.get(url2)
future10 = new_sess.get(url1)
new_re1 = future1.result().json()
new_re2 = future2.result().json()
new_re3 = future3.result().json()
new_re4 = future4.result().json()
new_re5 = future5.result().json()
new_re6 = future6.result().json()
new_re7 = future7.result().json()
new_re8 = future8.result().json()
new_re9 = future9.result().json()
new_re10 = future10.result().json()
new_end = time.time()
new_cost = new_end - new_start


new2_start = time.time()
future21 = new_sess.get(url1)
new_re21 = future21.result().json()
future22 = new_sess.get(url2)
new_re22 = future22.result().json()
future23 = new_sess.get(url1)
new_re23 = future23.result().json()
future24 = new_sess.get(url2)
new_re24 = future24.result().json()
future25 = new_sess.get(url1)
new_re25 = future25.result().json()
future26 = new_sess.get(url2)
new_re26 = future26.result().json()
future27 = new_sess.get(url1)
new_re27 = future27.result().json()
future28 = new_sess.get(url2)
new_re28 = future28.result().json()
future29 = new_sess.get(url1)
new_re29 = future29.result().json()
future210 = new_sess.get(url2)
new_re210 = future210.result().json()
new2_end = time.time()
new2_cost = new2_end - new2_start


new_start3 = time.time()
future1 = new_sess.get(url1)
future2 = new_sess.get(url2)
new_re1 = future1.result().json()
new_re2 = future2.result().json()
new_end3 = time.time()
new_cost3 = new_end3 - new_start3