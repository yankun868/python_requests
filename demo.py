import requests
import json
class port():
    def port_requests(self):
        self.session = requests.session()
        urltext = "https://poolapi.mempool.com/userService/userAuth"
        header = {'Content-Type':'application/json;charset=UTF-8'}
        data = {"login":"18530603710","password":"2908097jmg."}
        res = self.session.post(url = urltext,data=json.dumps(data),headers = header)
        print(res.text)
        url = "http://192.168.1.2:9009/admin/calculator/addBrand"
        header = {'Content-Type':'application/json;charset=UTF-8'}
        data = {"cn_name":"5","en_name":"5"}
        res = self.session.post(url = url,headers = header,data = json.dumps(data))
        print(res.text)

    def demo(self):
        a = "1"
        b = "21"
        if a in b:
            print("OK")
        else:
            print("ON")


if __name__ == '__main__':
    aa = port()
    # aa.port_requests()
    # aa.addpinpai()
    aa.demo()

