# -*- coding:UTF-8 -*-


import re



#切片

# str[beg:end]
# （下标从 0 开始）从下标为beg开始算起，切取到下标为 end-1 的元素，切取的区间为 [beg, end)
str = 'abcdefghijklmnopqrst'
print(str[3:5]) #de
# str[beg:end:step]
# 取 [beg, end) 之间的元素，每隔 step-1 个取一个
print(str[3:10:1]) #defghij
# str[beg:]
# 从下标为beg开始算起切取到结尾
print(str[3:]) #defghijklmnopqrst
# str[:end]
# 从下标为0开始切取到下标为end
print(str[:3]) #abc
# str[-beg:]
# 指从字符串的尾部开始计数(最末尾的字符记为-1)
print(str[-3:]) #rst

#无转义
# 在字符串前加 r/R
# 所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符
print(r'\n')  #\n

#字符串重复
# str * n, n * str
# n 为一个 int 数字
str = "hi"
print(str*2)   # hihi
print(2*str)   # hihi

#in操作(可用于循环、判断)
str = 'hello,world'
print('e' in str) #True
print('he' not in str) #False



#strip()函数用于且只能移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#去空格
str = ' hello world '
print(str)
# 去首尾空格
print(str.strip())  # hello world
# 去左侧空格
print(str.lstrip()) #hello world
# 去右侧空格
print(str.rstrip()) # hello world
#去'\n'
str = ' hello world\n'
print(str)
print(str.strip())  
print(str.lstrip()) 
print(str.rstrip()) 

#分隔字符串
str = ' a : b : c : d : e : f '
# 默认使用空格分隔
print(str.split())   # ['a', ':', 'b', ':', 'c', ':', 'd', ':', 'e', ':', 'f']
# 指定使用空格进行分隔，首尾如果有空格，则会出现在结果中
print(str.split(' ')) # ['', 'a', ':', 'b', ':', 'c', ':', 'd', ':', 'e', ':', 'f', '']
# 指定其他字符串进行分隔
print(str.split(':')) # [' a ', ' b ', ' c ', ' d ', ' e ', ' f ']
print(str.split('c :')) # [' a : b : ', ' d : e : f ']
str = 'mississippi'
print(str.rstrip('ip')) #mississ
# 取行, python 中把 "\r"，"\n"，"\r\n"，作为行分隔符
str = 'ab c\n\nde fg\rkl\r\n'
print(str.splitlines())  # ['ab c', '', 'de fg', 'kl']
print(str.splitlines(True))  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']


#拼接字符串
# str.join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str = '-'
seq = ("a", "b", "c"); # 字符串序列
print(str.join(seq)) # 'a-b-c'


#统计字符串里某个字符出现的次数
# str.count(sub, start= 0,end=len(string))
str = "thing example....wow!!!"
print(str.count('i', 0, 5))  # 1
print(str.count('e'))  # 2



#检测字符串中是否包含子字符串
# str.find(str, beg=0, end=len(string))
# 如果包含子字符串返回开始的索引值，否则返回-1。
str1 = "this is string example....wow!!!"
str2 = "exam"
print(str1.find(str2))      # 15
print(str1.find(str2,2))  # 15
#print(str1.find(str2, 40))  # -1

# str.index(str, beg=0, end=len(string))
# 如果包含子字符串返回开始的索引值，否则抛出异常。
print(str1.index(str2))    # 15
#print(str1.index(str2,16)) # 15
#print(str1.index(str2, 40))
# Traceback (most recent call last):
#   File "test.py", line 8, in
#   print str1.index(str2, 40);
#   ValueError: substring not found
# shell returned 1

print(str1.rfind(str2))
print(str1[15])
# tr.rindex(str, beg=0, end=len(string))


#判断字符串是否以指定前缀、后缀结尾
# str.startswith(str, beg=0,end=len(string))
# 检查字符串以指定子字符串开头，如果是则返回 True，否则返回 False
str = "this is string example....wow!!!"
print(str.startswith( 'this' )) # True
print(str.startswith( 'is',2,4))      # True

# str.endswith(suffix[, start[, end]])
# 以指定后缀结尾返回True，否则返回False
suffix = "wow!!!"
print(str.endswith(suffix)) # True
print(str.endswith(suffix,2,4)) #False


#根据指定的分隔符将字符串进行分割
# str.partition(del)
# 返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
str = "http://www.baidu.com/"
print(str.partition("://"))   # ('http', '://', 'www.baidu.com/')
print(str.rpartition("."))  # 从右边开始 ('http://www.baidu', '.', 'com/')



#替换字符串
# str.replace(old, new[, max])
# 字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str = "thing is example....wow!!! thisslly string";
print(str.replace("is", "was"))     # thing was example....wow!!! thwasslly string
print(str.replace("is", "was", 1)) # thing was example....wow!!! thwisslly string
# str.expandtabs(tabsize=8)
# 把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8



#检测字符串组成
# 检测数字
#str.isdigit()    # 检测字符串是否只由数字组成
#str.isnumeric()  # 检测字符串是否只由数字组成,这种方法是只针对unicode对象
#str.isdecimal()  # 检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
# 检测字母
#str.isalpha()   # 检测字符串是否只由字母组成
# 检测字母和数字
#str.isalnum()   # 检测字符串是否由字母和数字组成
# 检测其他
#str.isspace()   # 检测字符串是否只由空格组成
#str.islower()   # 检测字符串是否由小写字母组成
#str.isupper()   # 检测字符串中所有的字母是否都为大写
#str.istitle()   # 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写

#字符串处理
#str.capitalize()   # 将字符串的第一个字母变成大写,其他字母变小写
#str.lower()        # 转换字符串中所有大写字符为小写
#str.upper()        # 将字符串中的小写字母转为大写字母
#str.swapcase()     # 对字符串的大小写字母进行转换
#max(str)    # 返回字符串 str 中最大的字母
#min(str)    # 返回字符串 str 中最小的字母
#len(str)    # 返回字符串的长度
#str(arg) # 将 arg 转换为 string


#格式化输出
#居中填充
# str.center(width[, fillchar])
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
str = "this is string example....wow!!!"
print(str.center(40, 'a'))   # aaaathis is string  example....wow!!!aaaa


#靠右填充
# str.zfill(width)
# 返回指定长度的字符串，原字符串右对齐，前面填充0
str = "this is string example....wow!!!"
print(str.zfill(40))   # 00000000this is string example....wow!!!



#输出格式
print("My name is %s and weight is %d kg!" % ('Zara', 21))
# My name is Zara and weight is 21 kg!
print('%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2})
# Python has 002 quote types.
# str.format(*args, **kwargs)
print('{0}, {1}, {2}'.format('a', 'b', 'c'))  # a, b, c
print('{1}, {0}, {2}'.format('a', 'b', 'c')) # b, a, c




s = "China's Legend Holdings will split its several business arms to go public on stock markets, the group's president Zhu Linan said on Tuesday.该集团总裁朱利安周二表示，中国联想控股将分拆其多个业务部门在股市上市。"

# result = "".join(i for i in s if ord(i) < 256)
# print(result)

#匹配英文
#uncn = re.compile(r'[\u0061-\u007a,\u0020]')
#匹配非中文
#uncn = re.compile(r'[^\u4e00-\u9fa5]')
#匹配中文
uncn = re.compile(r'[\u4e00-\u9fa5]')
en = "".join(uncn.findall(s))
print(en)

 
# a = "我的English学的不好" 
# print(type ( a ) , len ( a ) , a) 

# b = unicode ( a, "utf-8" ) 
# print(type ( b ) , len ( b ) , b)