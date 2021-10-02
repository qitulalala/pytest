import requests
import json
import allure


class TestWeixin:
    def test_gettoken(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": 'wwec0c1629ebe40f45',
                "corpsecret": 'lK-JtaaAb-Y5A7Aw1s7AM6eVgzvmXW1c3zGxwTWLbYE'
            }
        }
        r = requests.request(**data)
        # print(r.json())
        token = r.json()['access_token']
        assert r.json()['errcode'] == 0
        return token

    def test_find(self):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": TestWeixin().test_gettoken()}
        }
        r = requests.request(**data)
        # print(r)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 0
        return r.json()

    def test_add(self):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            "params": {
                "access_token": TestWeixin().test_gettoken()
            },
            "json": {
                # "group_id": "GROUP_ID",
                "group_name": "apple",
                "order": 2,
                "tag": [{
                    "name": "greenapple",
                    "order": 1
                },
                    {
                        "name": "redapple",
                        "order": 2
                    }
                ]
            }
        }
        r = requests.request(**data)
        assert r.json()['errcode'] == 0
        # print(r)
        # return r.json()['tag_group'][0]['group_id']
        # return r.json()

    def test_edit(self):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            "params": {"access_token": TestWeixin().test_gettoken()},
            "json": {
                "id": TestWeixin.test_find(self)['tag_group'][0]['group_id'],
                "name": "banana",
                "order": 1,
            }
        }
        requests.request(**data)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # print(r.json())

    def test_del(self):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {"access_token": TestWeixin().test_gettoken(), 'debug': 1},
            "json": {
                "tag_id": [TestWeixin.test_find(self)['tag_group'][0]['tag'][0]['id']]
            }
        }
        r = requests.request(**data)
        print(r.json())
        # assert r.json()['errmsg'] == 'ok'
        # print(r.json())
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
