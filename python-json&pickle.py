#conding: utf-8

#Json模块提供了四个功能：dumps、dump、loads、load

# pickle模块提供了四个功能：dumps、dump、loads、load

#pickle 序列化
import pickle

data = {'K1':123,'k2':'Hello'}

p_str = pickle.dumps(data) # pickle.dumps 将数据通过特殊的形式转换位只有python语言认识的字符串
print (p_str)

a_str = pickle.loads(p_str) # pickle.loads 将只有python语言认识的字符串通过特殊形式转换成字符
print (a_str)

with open('res.pk','wb') as fp:
    pickle.dump(data,fp) # pickle.dump将数据通过特殊的形式转换位只有python语言认识的字符串，并写入文件

with open ('res.pk','rb') as fp:
    a_str=pickle.load(fp) # pickle.load 将文件中只有python语言认识的字符串通过特殊形式转换成字符
print (a_str)

#json 序列化

import json

j_data = {'K1':'kong','k2':'Hello'}

j_str = json.dumps(j_data)
print(j_str)

