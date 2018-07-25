#conding:utf-8

import re

f = open('info.txt','r',encoding='utf-8')
data = f.read()
phones = re.findall("[0-9]{11}",data)
print (phones)

# match如果查找到结果， 将返回一个 MatchObject，你可以查询 MatchObject 关于匹配字符串的相关信息了。MatchObject 实例也有几个方法和属性；最重要的那些如下所示：
# group() 返回被 RE 匹配的字符串
# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回一个元组包含匹配 (开始,结束) 的位置

obj = re.match('\d+','45345uu456asf')
if obj:
    print (obj.group())
    print (obj.start())
    print (obj.end())
    print (obj.span())
