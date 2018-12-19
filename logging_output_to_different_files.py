# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:36:20 2018

@author: fangyucheng
"""

import logging
formatter = logging.Formatter('%(asctime)s %(name)s: %(filename)s %(funcName)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
