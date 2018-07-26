#!__coding:utf-8_*_
#__author__:"Xianglei Kong"

import os

from core import db_handler

def acc_auth2(account,apassword):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)

    if


def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data['is_authebticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input ("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(account,password)