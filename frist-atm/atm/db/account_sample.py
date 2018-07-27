#!__coding:utf-8_*_
#__author__:"Xianglei Kong"

import json
import datetime
enroll_data = datetime.datetime.now().strftime('%Y-%m-%d')
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date':enroll_data,
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled
}