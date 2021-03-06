#coding:utf-8
#__author__:"Xianglei Kong"

import time
import os
import json
import re

from core import logger
from core import auth
from core.auth import login_required
from core import accounts
from core import transaction
from conf import settings

# temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authebticated':False,
    'account_data':None
}
#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')

def account_info(acc_data):
    print (acc_data)

@login_required
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
       Credit :    %s
       Balance:    %s''' % (account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print ("'\033[34;1mNew Balance:%s\033[0m" % new_balance['balance'])
        else:
            print ('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)
        if repay_amount == 'b':
            back_flag = True

def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance=''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s'''%(account_data['credit'],account_data['balance'])
    print (current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if withdraw_amount.isdigit() and len(withdraw_amount) > 0:
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw',withdraw_amount)
            if new_balance:
                print('''\033[31;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
        if withdraw_amount == 'b':
            back_flag = True

def transfer(acc_data):
    '''
    print current balance and let user do the transfer action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        trans_user = input('input the ID who you want transfer >>: ')
        trans_user_file = ("%s/%s/%s.json" % (settings.DATABASE['path'],settings.DATABASE['name'],trans_user))
        if os.path.isfile(trans_user_file):
            balance = input('input transfer balance>>: ').strip()
            if balance.isdigit() and len(balance) > 0:
                new_balance = transaction.make_transaction(trans_logger,account_data,'transfer',balance)
            if new_balance:
                print('''\033[31;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
                with open (trans_user_file,'r') as f:
                    trans_user_data = json.load(f)
                    transaction.make_transaction(trans_logger,trans_user_data,'repay',balance)
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % balance)
        else:
            print ("no such user")
        if trans_user ==  'b':
            back_flag = True
def pay_check(acc_data):
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES['transaction'])
    with open(log_file,'r') as f:
        log_file_info = f.read()
        acc_data_log = re.findall('.+account:%s.+' % acc_data['account_data']['id'],log_file_info)
        for line in acc_data_log:
            print (line)
def logout(acc_data):
    print ("have a nice day")
def interactive(acc_data):
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
    menu_dic = {
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':pay_check,
        '6':logout,
    }
    exit_flag = False
    while not exit_flag:
        print (menu)
        user_option = input(">>: ").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
            if user_option == '6':
                exit_flag = True
        else:
            print ("\033[31;1m Option does not exist!\033[0m")

def run():
    print ("weclome!!!!")
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authebticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)