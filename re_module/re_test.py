#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:07:29 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import re
import pandas as pd

result_list = []

text_list = []
with open('dates.txt') as file:
    for line in file:
        text_list.append(line)

count = 0

work_list = []

for line in text_list:
    text_dict = {"index": count,
                 "text": line}
    count += 1
    work_list.append(text_dict)

new_count = 0

for line in work_list:
    text = line['text']
    date = re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4,4}", text)
    if date != []:
        if len(date) == 2:
            date.remove(date[-1])
        print(date)
        date = ' '.join(date)
        line["date"] = date
        new_count += 1
        line['result'] = 1
        result_list.append(line)
    else:
        date = re.findall("[0-9]{1,2}-[0-9]{1,2}-[0-9]{4,4}", text)
        if date != []:
            print(date)
            date = ' '.join(date)
            line["date"] = date
            new_count += 1
            line['result'] = 1
            result_list.append(line)
        else:
            date = re.findall("[0-9]{1,2} [A-z]{3,12} [0-9]{4,4}", text)
            if date != []:
                print(date)
                date = ' '.join(date)
                line["date"] = date
                new_count += 1
                line['result'] = 1
                result_list.append(line)
            else:
                date = re.findall("[0-9]{1,2} [A-z]{3,12} [0-9]{4,4}", text)
                if date != []:
                    print(date)
                    date = ' '.join(date)
                    line["date"] = date
                    new_count += 1
                    line['result'] = 1
                    result_list.append(line)
                else:
                    date = re.findall("[A-z]{3,12} [0-9]{1,2}, [0-9]{4,4}", text)
                    if date != []:
                        print(date)
                        date = ' '.join(date)
                        line["date"] = date
                        new_count += 1
                        line['result'] = 1
                        result_list.append(line)
                    else:
                        date = re.findall("[A-z]{3,12} [0-9]{1,2} [0-9]{4,4}", text)
                        if date != []:
                            print(date)
                            date = ' '.join(date)
                            line["date"] = date
                            new_count += 1
                            line['result'] = 1
                            result_list.append(line)
                        else:
                            date = re.findall("[A-z]{3,12}. [0-9]{1,2}, [0-9]{4,4}", text)
                            if date != []:
                                print(date)
                                date = ' '.join(date)
                                line["date"] = date
                                new_count += 1
                                line['result'] = 1
                                result_list.append(line)
                            else:
                                date = re.findall("[A-z]{3,12} [0-9]{4,4}", text)
                                if date != []:
                                    print(date)
                                    date = ' '.join(date)
                                    line["date"] = date
                                    new_count += 1
                                    line['result'] = 1
                                    result_list.append(line)
                                else:
                                    date = re.findall("[A-z]{3,12}, [0-9]{4,4}", text)
                                    if date != []:
                                        print(date)
                                        date = ' '.join(date)
                                        line["date"] = date
                                        new_count += 1
                                        line['result'] = 1
                                        result_list.append(line)
                                    else:
                                        date = re.findall("[0-9]{1,2}/[0-9]{4,4}", text)
                                        if date != []:
                                            print(date)
                                            date = ' '.join(date)
                                            line["date"] = date
                                            new_count += 1
                                            line['result'] = 1
                                            result_list.append(line)
                                        else:
                                            date = re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,2}", text)
                                            if date != []:
                                                if len(date) == 2:
                                                    date.remove(date[-1])
                                                print(date)
                                                date = ' '.join(date)
                                                date = date[-2:]
                                                date = "19" +date
                                                line["date"] = date
                                                new_count += 1
                                                line['result'] = 1
                                                result_list.append(line)
                                            else:
                                                date = re.findall("[0-9]{1,2}-[0-9]{1,2}-[0-9]{2,2}", text)
                                                if date != []:
                                                    print(date)
                                                    date = ' '.join(date)
                                                    date = date[-2:]
                                                    date = "19" +date
                                                    line["date"] = date
                                                    new_count += 1
                                                    line['result'] = 1
                                                    result_list.append(line)
                                                else:
                                                    date = re.findall("[0-9]{4,4}", text)
                                                    if date != []:
                                                        print(date)
                                                        print(line)
                                                        date = ' '.join(date)
                                                        line["date"] = date
                                                        new_count += 1
                                                        line['result'] = 1
                                                        result_list.append(line)
                                                    else:
                                                        line["result"] = 0

new_result_list = []

for line in result_list:
    new_dict = {}
    date = line["date"]
    date = re.findall("[0-9]{4,4}", date)
    date = ' '.join(date)
    date = int(date)
    new_dict["index"] = line["index"]
    new_dict["date"] = date
    new_result_list.append(new_dict)

df = pd.DataFrame(new_result_list)
df['rank'] = df["date"].rank(ascending=False, method="min")

