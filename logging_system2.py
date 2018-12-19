# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:42:08 2018

@author: fangyucheng
"""

import logging

class MultiFileHandler(logging.FileHandler):

    def __init__(self, filename, mode, encoding=None, delay=0):
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)

    def emit(self, record):
        if self.should_change_file(record):
            self.change_file(record.file_id)
        logging.FileHandler.emit(self, record)

    def should_change_file(self, record):
        if not hasattr(record, 'file_id') or record.file_id == self.baseFilename:
             return False
        return True

    def change_file(self, file_id):
        self.stream.close()

        self.baseFilename = file_id
        self.stream = self._open()

if __name__ == '__main__':

    logger = logging.getLogger('request_logger')
    logger.setLevel(logging.DEBUG)    
    handler = MultiFileHandler(filename='out.log', mode='a')
    handler.setLevel(logging.DEBUG)    
    logger.addHandler(handler)

    # Log some messages to the original file
    logger.debug('debug message')
    logger.info('info message')