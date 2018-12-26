# -*- coding: utf-8 -*-
'''
正则表达式测试

'''

import re


# str = 'abc+10+20ac364abcd366a225b1abbcd55aabc'
# ''' 匹配*号前的字符0次或多次 '''
# Astr = re.findall("ab*",str)  #['ab', 'a', 'ab', 'a', 'abb', 'a', 'ab']
# ''' 匹配+号前的字符1次或多次 '''
# Astr = re.findall("ab+",str)  #['ab', 'ab', 'abb', 'ab']
# ''' 匹配?号前的字符1次或0次 '''
# Astr = re.findall("ab+",str)  #['ab', 'ab', 'abb', 'ab']
# ''' 匹配确定的 {n} 次'''
# Astr = re.findall('ab{2}',str)

# print(Astr)



# str = 'acbacb'
# # "*?"  重复任意次，但尽可能少重复 
# Astr = re.findall('a.*?b',str) #['acb', 'acb']
# # "+?" 重复1次或更多次，但尽可能少重复
# Astr = re.findall('a.+?b',str) #['acb', 'acb']
# # "??" 重复0次或1次，但尽可能少重复
# Astr = re.findall('a.??b',str) #['acb', 'acb']
# print(Astr)

# a = 'abc+10 + 20'
# b = 'abc+10+20'
# regex1 = re.compile('\d+\s*[+]\s*\d+') #对正则表达式进行编译，\d+表示匹配一个或多个数字，\s*表示匹配0个或多个空格，[]里面为字符集
# print(regex1.search(a).group())  # 10 + 20
# print(regex1.search(b).group())  # 10+20

# regex2 = re.compile(r'(\d+)([+])(\d+)') #('10', '+', '20')

# print(regex2.search(b).groups())



#匹配以数字开头以数字结尾
a = '1abc+10+20'
regex1 = re.compile(r'^\d.*\d$')
print(regex1.search(a).group())    # 1abc+10+20

#groupdict与（）搭配使用
print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict() )   #{'province': '3714', 'city': '81', 'birthday': '1993'}



#split使用
a = '1abc+10+20'
regex1 = re.compile(r'\+')  #['1abc', '10', '20']
print(regex1.split(a)) 

#=>print(re.split(r'\+',a))


#sub使用 *号替换+号
a = '1abc+10+20'
regex1 = re.compile(r'\+')
print(regex1.sub('*',a))  #1abc*10*20
print(regex1.sub('*',a,1)) #1abc*10+20

#^与[]搭配
regex1 = re.compile('[^abc]')
print(regex1.findall(a))  # ['1', '+', '1', '0', '+', '2', '0']
print(regex1.search(a).group()) #1
print(regex1.match(a).group())  #1



str = "a0b a1b a2b a3b a123b"
Astr = re.findall('a[123]b',str) #['acb', 'acb']
print(Astr)