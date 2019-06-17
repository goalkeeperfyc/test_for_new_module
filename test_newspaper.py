# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:46:52 2019

@author: tn_yucheng.fang
"""

from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)

article.download()

article.parse()

print(article.authors)
print(article.text)

article.nlp()

print(article.keywords)