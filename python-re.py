#conding:utf-8

import re

f = open('info.txt','r',encoding='utf-8')
data = f.read()
phones = re.findall("[0-9]{11}",data)
print (phones)

#从起始位置开始根据模型去字符串中匹配指定内容，匹配单个
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

#search()方法与match()方法类似,search 不是从头匹配
obj = re.search('\d+','45345uu456asf')
if obj:
    print (obj.group())
    print (obj.start())
    print (obj.end())
    print (obj.span())

#match and search均用于匹配单值，即：只能匹配字符串中的一个，如果想要匹配到字符串中所有符合条件的元素，则需要使用 findall。
#re.findall(pattern, string, flags=0)

obj = re.findall('\d+','45345uu456asf')
print (obj)


#用于替换匹配的字符串,相比于str.replace功能更加强大
#re.sub(pattern, repl, string, count=0, flags=0)

str = re.sub('[a-z]+','sb','武配齐是abc123asd')   #将匹配的数字替换成|，替换两个，若没有count则全部替换
print (str)

str = re.sub('\d+','|','alex22wupeiqi33oldboy55',count=2)# count=2 则表示匹配两次
print (str)

#re.split(pattern, string, maxsplit=0, flags=0)

s='9-2*5/3+7/3*99/4*2998+10*568/14'
s_s = re.split('[\-\*\/\+]',s)#maxsplit默认全部匹配
print (s_s)

s_s = re.split('[\-\*\/\+]',s,3)
print (s_s)

# re.fullmatch(pattern, string, flags=0)
# 整个字符串匹配成功就返回re object, 否则返回None

r_str=re.fullmatch('\w+@\w+.(com|cn|edu)',"kongxainglei@qq.com")
if r_str:
    print (r_str.group())

#实例：
with open('text-1.txt','r',encoding='utf-8') as f:
    line = f.read()
    print (line)
    meil = re.search('\w+.com',line)
    print (meil.group())