import json
import requests


class Public:
    def __init__(self):
        self.holder = self.get_token()

    def send(self, par):
        r = requests.request(**par)
        # 其它操作，例如格式化输出，日志等
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def get_token(self):
        r = requests.request('post', 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                             params={"corpid": 'wwec0c1629ebe40f45',
                                     "corpsecret": 'lK-JtaaAb-Y5A7Aw1s7AM6eVgzvmXW1c3zGxwTWLbYE'})
        return r.json()['access_token']


# if __name__ == '__main__':
#     print(BaseApi().get_token())
