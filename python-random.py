# coding:utf-8
import random

#返回1-10之间的一个随机数，不包括10
print (random.randrange(1,10))

#返回1-10之间的一个随机数，包括10
print (random.randint(1,10))

#随机选取0到100间的2的倍数
print (random.randrange(0,100,2))

#返回一个随机浮点数
print (random.random())

#返回一个给定数据集合中的随机字符
print (random.choice('abce3#$@1'))

#从多个字符中选取特定数量的字符,本例为选取3个字符
print (random.sample('123adfrtyjgk',3))

#生成随机字符串(字母 + 数字)
import string
str = ''.join(random.sample(string.ascii_letters + string.digits,16))
print (str)

#洗牌
a = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)