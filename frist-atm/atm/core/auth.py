#!__coding:utf-8_*_
#__author__:"Xianglei Kong"

import os
import time

from core import db_handler

def acc_auth2(account,password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)

    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print ("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else:   # passed the authentication
            return data

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
        if auth:
            user_data['is_authebticated'] = True
            user_data['account_id'] = account
            print ("hello nice to meet you!!!")
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()