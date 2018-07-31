#coding:utf-8
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
    user_account = input('\033[32;2m input  the id you want change >>:  \033[0m')
    user_file = ("%s/%s/%s.json" % (settings.DATABASE["path"], settings.DATABASE["name"], user_account))
    if os.path.isfile(user_file):
        new_credit = input("please input the money >>: ").strip()
        if new_credit.isdigit() and len(new_credit) > 0:
            with open (user_file,'r') as f:
                user_info = json.load(f)
                user_info['credit'] = new_credit
            with open(user_file, 'w') as f:
                json.dump(user_info,f)
        else:
            print ('\033[31;1m please input a digit!! \033[0m')
    else:
        print ("\033[31;1m No such user! \033[0m")
def frozen():
    user_account = input('\033[32;2m input  the id you want frozen >>:  \033[0m')
    user_file = ("%s/%s/%s.json" % (settings.DATABASE["path"], settings.DATABASE["name"], user_account))
    if os.path.isfile(user_file):
        print('''input 1 to frozen id\ninput 0 to thaw id''')
        status = input('>>: ')
        with open (user_file,'r') as f:
            user_info = json.load(f)
            user_info['status'] = status
        with open(user_file,'w') as f:
            json.dump(user_info, f)
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
            manage_dic[manage_option]()
