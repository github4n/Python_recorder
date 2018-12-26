# -*- coding: utf-8 -*-
'''
将文档中的奇偶行转换顺序
'''


import linecache


def ji_ou_change(file_b,file_a):
    f_be=open(file_b,'r',encoding='utf-8')
    f_af=open(file_a,'w',encoding='utf-8')
    line_num=len(f_be.readlines())
    for i in range(1 , line_num + 1):
        if i % 2 == 0:
            line = linecache.getline(file_b,i-1).strip()
            f_af.write(line + '\n')
        elif i % 2 == 1:
            line = linecache.getline(file_b,i+1).strip()
            f_af.write(line + '\n')
    f_be.close()
    f_af.close()

if __name__== "__main__":
    ji_ou_change("before.txt","after.txt")