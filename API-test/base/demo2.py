#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
import json
class RunMain:
    # 构造函数
    # def __init__(self,url,method,data=None):
    #     res = self.runmain(url,method,data)
    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def send_post(self,url,data):
        res = requests.post(url=url, data=data).json()
        # 格式化处理：json.dumps(indent=None(默认none,前面空格，,sort_keys=True sort_keys，按abcd排序))
        return json.dumps(res, indent=2, sort_keys=True)
        # print(res['CODE'])
    def runmain(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return json.loads(res)
# if __name__ == '__main__':
    # get方法
    # run = RunMain()
    # url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    # data = {
    #     'cart':'11'
    # }

    # url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
    # data = {
    #     "language": "EN",
    #     "platform": "3000",
    #     "remote_addr": "13.230.65.62",
    #     "userid": "",
    #     "subchannel": "10004",
    #     "casinoversion": "2.7.0",
    #     "version": "2.7.0",
    #     "pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
    #     "usercheck ": "",
    #     "username ": "",
    #     "pushproject ": "curacao ",
    #     "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
    # }
    # run = RunMain(url,'POST',data)
    # print(run.runmain(url,'POST',data))




# url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
# data ={
# 	"language": "EN",
#     "platform": "3000",
# 	"remote_addr": "13.230.65.62",
# 	"userid": "",
# 	"subchannel": "10004",
# 	"casinoversion": "2.7.0",
# 	"version": "2.7.0",
# 	"pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
#     "usercheck ": "",
#     "username ": "",
#     "pushproject ": "curacao ",
#     "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
# }












