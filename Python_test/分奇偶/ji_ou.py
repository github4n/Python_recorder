#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
python读取文件，偶数行输出一个文件，奇数行输出一个文件

'''
def jiou(file_z,file_j,file_o):
    f_zo=open(file_z,'r',encoding='utf-8')
    f_ji=open(file_j,'w',encoding='utf-8')
    f_ou=open(file_o,'w',encoding='utf-8')
    n=0
    lines=f_zo.readlines()
    for line in lines:
        n += 1
        if n % 2 == 0:
            f_ou.write(line)
        else:
            f_ji.write(line)
    f_zo.close()
    f_ji.close()
    f_ou.close()


jiou("zong.txt","ji.txt","ou.txt")


