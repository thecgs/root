"""
2019/11/02
陈桂森
基于百度翻译API python3的demo改的
用于翻译出文本文件
百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
coding=utf-8
"""

import http.client
import hashlib
import urllib
import random
import time
import json

appid = '20170625000060211'  # 填写你的appid
secretKey = 'Xl9CEkxjT2l9rc_BydRx'  # 填写你的密钥

httpClient = None
url = '/api/trans/vip/translate'

fromLang = 'auto'   #原文语种
toLang = 'auto'   #译文语种
salt = random.randint(32768, 65536)
sub = input('请输入翻译文件名：')
i = open(sub, 'a+', encoding='utf-8')
i.seek(0)

for q in i:
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = url + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    time.sleep(0.8)#延迟翻译，否则丢包
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print(f'输入的内容是：%s \n翻译的结果是：%s' % (result['trans_result'][0]['src'], result['trans_result'][0]['dst']))
    except Exception as e:
        pass
    finally:
        if httpClient:
            httpClient.close()
