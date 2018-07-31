#!_*_coding:utf-8_*_
#__author__:"Xianglei Kong"

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# sys.path.append('%s\\atm' % base_dir)
print (sys.path)

from atm.core import main

if __name__ == '__main__':
    main.run()