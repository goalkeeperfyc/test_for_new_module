# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:32:25 2018

@author: fangyucheng
"""


import zipfile
from os.path import basename

zip_file = zipfile.ZipFile('test.zip', 'w', compression=zipfile.ZIP_DEFLATED)

zip_file.write('D:/python_code/all_kinds_of_test/test_input.py', basename('D:/python_code/all_kinds_of_test/test_input.py'))
zip_file.write('D:/python_code/all_kinds_of_test/test_logging.py', basename('D:/python_code/all_kinds_of_test/test_logging.py'))
zip_file.close()