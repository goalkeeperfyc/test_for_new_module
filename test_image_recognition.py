# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:23:04 2018

@author: fangyucheng
"""

import time
from aip import AipOcr
from crawler_sys.utils import Metaorphosis as meta
 
APP_ID = '11746742'
API_KEY = 'YqKWaR7LWin31OSXPOtfoIAB'
SECRET_KEY = 'UKjmvp6hbxB1fX7Gxg4RP79Xw5hg5a0Q'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    result_lst = []
    count = 570
    while count <= 686:
        file_name = 'D:/add_target_releaser/image_recognition/Capture/photo' + str(count) +'.jpg'
        image = get_file_content(file_name)
        words_in_image = client.basicGeneral(image)
        words_lst = words_in_image['words_result']
        cut_position = 0
        for line in words_lst:
            line_words = line['words']
            if '关注' in line_words:
                cut_position = words_lst.index(line)
                break
        words_lst = words_lst[cut_position+1:]
        for line in words_lst:
            line_words = line['words']
            result_lst.append(line_words)
        print(file_name)
        count += 1
