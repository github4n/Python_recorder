# -*- coding:utf-8 -*-


import re


def split_zh(file1,file2,file3):
	file_zong = open(file1,'r',encoding='utf-8')
	file_zh = open(file2,'w',encoding='utf-8')
	file_ot = open(file3,'w',encoding='utf-8')
	text = file_zong.readlines()
	for line in text:
		#匹配英文
		#uncn = re.compile(r'[\u0061-\u007a,\u0020]')
		
		#匹配中文
		uncn_zh = re.compile(r'[\u4e00-\u9fa5]')
		zh = "".join(uncn_zh.findall(line)).strip()
		print(zh)
		file_zh.write(zh + '\n')
		#匹配非中文
		uncn_ot = re.compile(r'[^\u4e00-\u9fa5]')
		ot = "".join(uncn_ot.findall(line)).strip()
		print(ot)
		file_ot.write(ot + '\n')
	file_zong.close()
	file_zh.close()
	file_ot.close()


if __name__ == '__main__':
	split_zh('zong.txt','zh.txt','not_zh.txt')
