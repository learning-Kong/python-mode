#coding:utf-8
#__author__:"Xianglei Kong"

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print (base_dir)
from core import main

if __name__ == '__main__':
    main.run()