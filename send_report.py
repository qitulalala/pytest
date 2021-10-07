import datetime
import json
import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://2934679630:Mm123456@47.93.5.75:9000/job/helloword/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
                    '312d2a9b69969e261495b8927067bbf18b1874344d7a7d85d35e5677e08a6de5'
        self.error = self.get_allure()

    def get_allure(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号jenkisn5,密码xxxxx",
                    "title": "qitulalala" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://2934679630:Mm123456@47.93.5.75:9000/job/helloword/allure"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
