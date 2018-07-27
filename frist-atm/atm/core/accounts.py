#!_*_coding:utf-8_*_
#__author__:"Xianglei Kong"


import core import db_handler
import conf import settings

def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account_id)
    return data
def dump_account(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)

    return Ture