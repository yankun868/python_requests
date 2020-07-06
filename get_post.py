import requests
import json
# from 接口.excle_index import *
class g_p():
    def __init__(self):
        self.session = requests.session()
    def login(self):
        #默认登录获取token
        header = {'Content-Type':'application/json;charset=UTF-8'}
        url = "https://poolapi.mempool.com/userService/userAuth"
        data = {"login":"17347786577","password":"yk123456."}
        aa = self.session.post(url = url,headers = header,data=json.dumps(data))
        print(aa.text)
    def get_way(self,url,data,header):
        res = self.session.get(url = url,data = json.dumps(data),headers =header)
        return res
    def post_way(self,url,data,header):
        a = json.loads(data)
        b = json.loads(header)
        res1 = self.session.post(url=url,headers = b,data=json.dumps(a))
        return res1.text
    def post_way1(self):
        url = 'https://poolapi.mempool.com/userService/userAuth'
        data = {"login":"17347786577","password":"yk123456."}
        header = {'Content-Type':'application/json;charset=UTF-8'}
        res = requests.post(url= url, data=json.dumps(data), headers=header)
        return res.text

# if __name__ == '__main__':
#     url = 'https://poolapi.mempool.com/userService/userAuth'
#     data = {"login":"18530603710","password":"2908097jmg."}
#     header = {'Content-Type':'application/json;charset=UTF-8'}
#     aa = g_p().post_way(url,data,header)
#     print(aa)
    # g_p().login()

