# -*- coding:utf-8 -*-



def cut(file1,file2):
	rtext = open(file1,'r',encoding='utf-8')
	wtext = open(file2,'w',encoding='utf-8')
	num = 0
	lines = rtext.readlines()
	for line in lines:
		num = num + 1
		if(num <= 20000):
			wtext.write(line)
		else:
			break
	rtext.close()
	wtext.close()

if __name__ == '__main__':
	cut('en-hi.en211621','en-hi.en20000')

