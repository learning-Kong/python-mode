#!_*_coding:utf-8_*_
#__author__:"Xianglei Kong"

import os
import sys
import datetime
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from db import account_sample
from conf import settings

def add_account():
    user_account = input("\033[31;2muser_account: \033[0m").strip()
    user_password = input("\033[31;2muser_password: \033[0m").strip()
    user_file = ("%s/%s/%s.json" % (settings.DATABASE["path"],settings.DATABASE["name"],user_account))
    print (user_file)
    print
    if os.path.isfile(user_file):
        print ("The account is exit!")
        return
    else:
        enroll_data = datetime.datetime.now().strftime('%Y-%m-%d')
        account_sample.acc_dic['id'] = user_account
        account_sample.acc_dic['password'] = user_password
        account_sample.acc_dic['enroll_date'] = enroll_data
        print (account_sample.acc_dic)
        with open(user_file,'w') as f:
            json.dump(account_sample.acc_dic,f)
def change_credit():
    pass
def frozen():
    pass
manage_info = '''\033[31;2m------- welcome manager -------
    input 1: add account
    input 2: change Credit
    input 3: frozen account 
    input 4: logout\033[0m'''

manage_dic = {
    '1':add_account,
    '2':change_credit,
    '3':frozen,
    '4':'logout'
}
exit_flags = False
while not exit_flags:
    print(manage_info)
    manage_option = input(">>: ").strip()
    if manage_option in manage_dic:
        if manage_option == '4':
            print ('see you')
            exit_flags = True
        else:
            manage_dic["1"]()
            #manage_dic[manage_option]()
