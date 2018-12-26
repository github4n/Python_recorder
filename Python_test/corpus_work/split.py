# -*- coding:UTF-8 -*-


import re

def split_corpus(input,output):
	with open(input,'r',encoding='UTF-8') as rfile:
		lines = rfile.readlines()
		for line in lines:
			result = line.split('\t')
			result = '\n'.join(result)
			with open(output,'a',encoding='UTF-8') as wfile:
				print(result)
				wfile.write(result)

if __name__== "__main__":
	split_corpus('input.txt','output.txt')