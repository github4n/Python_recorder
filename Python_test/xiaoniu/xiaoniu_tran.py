# -*- coding: utf-8 -*-


import requests
import json
import sys



def translate(input,output):
  with open(input,'r',encoding='utf-8') as rfile:
    lines = rfile.readlines()
    for line in lines:
      line = line.strip()
      apikey = '3aec701a3e5a5f0614df795eeffa67e8'
      # host = 'http://api.niutrans.vip'
      # path = '/NiuTransServer/translation'
      # method = 'post'
      # querys = 'from=en&to=zh&src_text=line&apikey='+apikey
      translate_url = 'http://api.niutrans.vip/NiuTransServer/translation'
      headers = {
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
            }
      data = {
      'src_text':line,
      'from':'zh',
      'to':'en',
      'apikey':apikey
      }
      #translate_url = host + path + '?' + querys
      response = requests.post(url=translate_url, data=data, headers=headers, timeout=5.1)
      content = response.json()
      result = content['tgt_text']
      if (content):
        print(result)
        with open(output,'a',encoding='utf-8') as wfile:
            wfile.write(result)       
      else:
        print('no')



if __name__== "__main__":
    #translate(sys.argv[0], sys.argv[1], sys.argv[2])
    translate('input.txt','output.txt')