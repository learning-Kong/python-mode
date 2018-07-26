#conding:utf-8
import sys
import time

print (sys.path)

exp_time_stamp = time.mktime(time.strptime("2021-01-01","%Y-%m-%d"))
print (exp_time_stamp)
print (time.time())