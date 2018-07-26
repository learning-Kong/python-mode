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

def interactive(user_data):
    '''
    interact with user
    :return:
    '''
    menu = '''
    \033[32;1m
    1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m
    '''
    print (menu)


def run():
    print ("weclome!!!!")
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authebticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)