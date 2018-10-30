# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:44:27 2018

@author: fangyucheng
"""


import re

midstep='\n(function() {\n    var a = document.getElementsByTagName(\'html\')[0];\n    if (a && typeof a.className == "string" && a.className.indexOf("lte_ie8") > -1) {\n        var s = "CSS1Compat" == document.compatMode ? document.documentElement.clientWidth : document.body.clientWidth,\n            b = a.className;\n        if (s < 1279) {\n            a.className = b.replace(/(?:^|s)screen_ms(?!S)/g, \'\') + " screen_xs";\n        } else if (s < 1599) {\n            a.className = b.replace(/(?:^|s)screen_xs(?!S)/g, \'\') + " screen_ms";\n        } else {\n            a.className = b.replace(/(?:^|s)screen_xs(?!S)/g, \'\').replace(/(?:^|s)screen_ms(?!S)/g, \'\');\n        }\n    }\n})();\nvar LIST_INFO = {"vid":["b0369a2flr9","b0510nyzinv","d055888cxvg","h05064f6b40","i0542qwoo3s","j0369nsieqm","k0550a4tedq","m0369zu71m9","o0523abh2jo","t03378alh4e","u03694ecjqa","v03695mij8g","w05265heocx","w0536ntxrwv","w0560xq8lug","y03699t5434","n0523817exf","n0540kzdate","z0010RmCbc6"],"data":{"e0364wllbk4":{"publish_date":null,"leading_actor_id":null,"duration":398,"cover_list":null,"guests":null,"race_teams_id":null,"type_name":"纪录片","tag":null,"singer_id":null,"episode":null,"race_stars_id":null,"srcsite_name":null,"type":null,"title":"国家相册 第（6）集：山就在那里","leading_actor":null,"show_type":"1","singer_name":null,"danmu_status":null,"second_title":null,"positive_trailer":null,"athlete":null,"mv_stars":null,"c_full":null,"update_flag":null,"desc":null,"pioneer_tag":null,"begin_time":null,"relative_covers":null,"upload_qq":2602608558,"category_map":[],"is_trailer":null,"stars_name":null,"pic_640_360":"http://puui.qpic.cn/vpic/0/e0364wllbk4.png/0","c_title_segment":null,"guests_id":null,"presenter_id":null,"upload_src":null,"athlete_id":null,"costar_id":null,"relative_stars_id":null,"relative_stars":null,"drm":null,"modify_time":null,"tail_time":null,"valid_tag_id":null,"vid":"e0364wllbk4","pic_url":null,"costar":null,"race_teams_name":null,"c_title_output":null,"director_id":null,"title_en":null,"stars":null,"danmu":null,"mv_stars_id":null,"playright":null,"presenter":null,"race_stars":null,"view_all_count":68,"c_tags_flag":0,"c_has_adv_danmu":null,"head_time":null,"state":null,"copyright_id":null,"pic160x90":"http://puui.qpic.cn/vpic/0/e0364wllbk4_160_90_3.jpg/0","director":null,"famous_id":null,"pioneer_tag_ids":null,"trytime":null,"famous_actor":null,"video_checkup_time":"2017-01-09 19:32:37","":null,"isFull":false,"from1006":true,"video_type":3,"rela_cover":{"positiveCover":{},"largestCover":{}}}},"firseClipListVid":""}\n\n// 进video的都属于A方案\nvar AB_PLAN = "A";\n\n\n/*\n * 评论浮层会用到的COVER_INFO\n * \n * shywang(王帅) 2017-12-25 15:06:25\n * COVER_INFO.movie_comment_set\n * COVER_INFO.id\n */\n\n\nvar COVER_INFO = {\n    payInfo: {},\n    yearAndArea: {}\n};\nvar COLUMN_INFO = {};\n\nvar VIDEO_INFO = {"publish_date":null,"leading_actor_id":null,"duration":398,"cover_list":null,"guests":null,"race_teams_id":null,"type_name":"纪录片","tag":null,"singer_id":null,"episode":null,"race_stars_id":null,"srcsite_name":null,"type":null,"title":"国家相册 第（6）集：山就在那里","leading_actor":null,"show_type":"1","singer_name":null,"danmu_status":null,"second_title":null,"positive_trailer":null,"athlete":null,"mv_stars":null,"c_full":null,"update_flag":null,"desc":null,"pioneer_tag":null,"begin_time":null,"relative_covers":null,"upload_qq":2602608558,"category_map":[],"is_trailer":null,"stars_name":null,"pic_640_360":"http://puui.qpic.cn/vpic/0/e0364wllbk4.png/0","c_title_segment":null,"guests_id":null,"presenter_id":null,"upload_src":null,"athlete_id":null,"costar_id":null,"relative_stars_id":null,"relative_stars":null,"drm":null,"modify_time":null,"tail_time":null,"valid_tag_id":null,"vid":"e0364wllbk4","pic_url":null,"costar":null,"race_teams_name":null,"c_title_output":null,"director_id":null,"title_en":null,"stars":null,"danmu":null,"mv_stars_id":null,"playright":null,"presenter":null,"race_stars":null,"view_all_count":68,"c_tags_flag":0,"c_has_adv_danmu":null,"head_time":null,"state":null,"copyright_id":null,"pic160x90":"http://puui.qpic.cn/vpic/0/e0364wllbk4_160_90_3.jpg/0","director":null,"famous_id":null,"pioneer_tag_ids":null,"trytime":null,"famous_actor":null,"video_checkup_time":"2017-01-09 19:32:37","":null,"isFull":false,"from1006":true,"video_type":3,"rela_cover":{"positiveCover":{},"largestCover":{}}}\n'
try:
    duration = re.findall(r'"duration":[0-9]{1,10}', ','.join(re.findall(r'VIDEO_INFO.*"duration":[0-9]{1,10}', midstep)))[0].split(':')[1]
except:
     print('Catched exception, didn\'t find duration in var VIDEO_INFO')
     duration=0
try:
    playcount = re.findall(r'"view_all_count":[0-9]{1,10}', ','.join(re.findall(r'VIDEO_INFO.*"view_all_count":[0-9]{1,10}', midstep)))[0].split(':')[1]
except:
    print('Catched exception, didn\'t find view_all_count in var VIDEO_INFO')
    playcount=0
    
midstep2='\n(function() {\n    var a = document.getElementsByTagName(\'html\')[0];\n    if (a && typeof a.className == "string" && a.className.indexOf("lte_ie8") > -1) {\n        var s = "CSS1Compat" == document.compatMode ? document.documentElement.clientWidth : document.body.clientWidth,\n            b = a.className;\n        if (s < 1279) {\n            a.className = b.replace(/(?:^|s)screen_ms(?!S)/g, \'\') + " screen_xs";\n        } else if (s < 1599) {\n            a.className = b.replace(/(?:^|s)screen_xs(?!S)/g, \'\') + " screen_ms";\n        } else {\n            a.className = b.replace(/(?:^|s)screen_xs(?!S)/g, \'\').replace(/(?:^|s)screen_ms(?!S)/g, \'\');\n        }\n    }\n})();\nvar LIST_INFO = {"vid":["t0346xuqhdq","n0540kzdate","c0500j8j4c3","7JJV3cUucYC","83Lq9ock762","8BRRiFTeXO7","8Yw9pH2Y0Fp","f0502jvwubt","b0526ngooge","e0524untu5v","g05512935dd","l0535bu7ecr","r0518o8pi1u","s0555kge0fj","w0567mp17kw","a0502ush8le","b0506fi0f4b","b0536fppszx","b0557ba4vv3","d0519e9k7ja"],"data":{"c0563uq17zy":{"publish_date":"2010-01-01 00:00:00","leading_actor_id":null,"duration":"315","cover_list":[],"guests":null,"race_teams_id":null,"type_name":"纪录片","tag":["国家相册","新华社","希望工程"],"singer_id":null,"episode":"0","race_stars_id":null,"srcsite_name":"","type":9,"title":"《国家相册》第80集：希望工程","leading_actor":null,"show_type":"1","singer_name":null,"danmu_status":1,"second_title":"","positive_trailer":0,"athlete":null,"mv_stars":null,"c_full":0,"update_flag":null,"desc":"又到开学时，请翻开本期《国家相册》，细细体味上学路上的那些爱与希望。","pioneer_tag":"社会纪实+希望小学+国家相册+国内","begin_time":"0","relative_covers":[],"upload_qq":"2208733102","category_map":[10722,"片花",1113,"国产纪录片",9,"纪录片"],"is_trailer":0,"stars_name":null,"pic_640_360":"http://puui.qpic.cn/vpic/0/c0563uq17zy.png/0","c_title_segment":"0|0","guests_id":null,"presenter_id":null,"upload_src":"108","athlete_id":null,"costar_id":null,"relative_stars_id":null,"relative_stars":null,"drm":0,"modify_time":"2018-03-04 16:03:20","tail_time":0,"valid_tag_id":"+644734+9659931+","vid":"c0563uq17zy","pic_url":"","costar":null,"race_teams_name":null,"c_title_output":"《国家相册》第80集：希望工程","director_id":[],"title_en":null,"stars":null,"danmu":1,"mv_stars_id":null,"playright":["1","2","3","4","5","8","9","10","18","20","40","57","61"],"presenter":null,"race_stars":null,"view_all_count":479338,"c_tags_flag":1,"c_has_adv_danmu":null,"head_time":0,"state":4,"copyright_id":"107","pic160x90":"http://puui.qpic.cn/vpic/0/c0563uq17zy_160_90_3.jpg/0","director":[],"famous_id":null,"pioneer_tag_ids":"9659931+644734+55734973+55783145+","trytime":null,"famous_actor":null,"video_checkup_time":"2018-03-04 09:16:18","":null,"isFull":false,"video_type":9,"from1006":true,"rela_cover":{"positiveCover":{},"largestCover":{}}}},"firseClipListVid":""}\n\n// 进video的都属于A方案\nvar AB_PLAN = "A";\n\n\n/*\n * 评论浮层会用到的COVER_INFO\n * \n * shywang(王帅) 2017-12-25 15:06:25\n * COVER_INFO.movie_comment_set\n * COVER_INFO.id\n */\n\n\nvar COVER_INFO = {\n    payInfo: {},\n    yearAndArea: {}\n};\nvar COLUMN_INFO = {};\n\nvar VIDEO_INFO = {"publish_date":"2010-01-01 00:00:00","leading_actor_id":null,"duration":"315","cover_list":[],"guests":null,"race_teams_id":null,"type_name":"纪录片","tag":["国家相册","新华社","希望工程"],"singer_id":null,"episode":"0","race_stars_id":null,"srcsite_name":"","type":9,"title":"《国家相册》第80集：希望工程","leading_actor":null,"show_type":"1","singer_name":null,"danmu_status":1,"second_title":"","positive_trailer":0,"athlete":null,"mv_stars":null,"c_full":0,"update_flag":null,"desc":"又到开学时，请翻开本期《国家相册》，细细体味上学路上的那些爱与希望。","pioneer_tag":"社会纪实+希望小学+国家相册+国内","begin_time":"0","relative_covers":[],"upload_qq":"2208733102","category_map":[10722,"片花",1113,"国产纪录片",9,"纪录片"],"is_trailer":0,"stars_name":null,"pic_640_360":"http://puui.qpic.cn/vpic/0/c0563uq17zy.png/0","c_title_segment":"0|0","guests_id":null,"presenter_id":null,"upload_src":"108","athlete_id":null,"costar_id":null,"relative_stars_id":null,"relative_stars":null,"drm":0,"modify_time":"2018-03-04 16:03:20","tail_time":0,"valid_tag_id":"+644734+9659931+","vid":"c0563uq17zy","pic_url":"","costar":null,"race_teams_name":null,"c_title_output":"《国家相册》第80集：希望工程","director_id":[],"title_en":null,"stars":null,"danmu":1,"mv_stars_id":null,"playright":["1","2","3","4","5","8","9","10","18","20","40","57","61"],"presenter":null,"race_stars":null,"view_all_count":479338,"c_tags_flag":1,"c_has_adv_danmu":null,"head_time":0,"state":4,"copyright_id":"107","pic160x90":"http://puui.qpic.cn/vpic/0/c0563uq17zy_160_90_3.jpg/0","director":[],"famous_id":null,"pioneer_tag_ids":"9659931+644734+55734973+55783145+","trytime":null,"famous_actor":null,"video_checkup_time":"2018-03-04 09:16:18","":null,"isFull":false,"video_type":9,"from1006":true,"rela_cover":{"positiveCover":{},"largestCover":{}}}\n'
#midstep2 playcount能得到，但是duration报错 
#IndexError: list index out of range