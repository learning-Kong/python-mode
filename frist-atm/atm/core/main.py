#!__coding:utf-8_*_
#__author__:"Xianglei Kong"

import time

from core import logger
from core import auth


user_data = {
    'account_id':None,
    'is_authebticated':False,
    'account_data':None
}

#access logger
access_logger = logger.logger('access')

def run():
    print ("weclome!!!!")
    acc_data = auth.acc_login(user_data,access_logger)