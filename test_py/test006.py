# todo 7. pytest fixture 参数传递 params

import datetime
import json

import requests
import pytest

# @pytest.fixture()
# def time_data():
#     time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     return time
#
#
# param_test = [{
#     "case": "serach a word :haha",
#     "headers": {},
#     "querystring": {
#         "wd": "hah"
#     },
#     "payload": {},
#     "expected": {
#         "status_code": 200
#     }
# },
#     {
#         "case": "serach a word2 :kuku",
#         "headers": {},
#         "querystring": {
#             "wd": "kuku"
#         },
#         "payload": {},
#         "expected": {
#             "status_code": 200
#         }},
#
#     {
#         "case": "serach a word3 :xiaoyulaoshi",
#         "headers": {},
#         "querystring": {
#             "wd": "xiaoyulaoshi"
#         },
#         "payload": {},
#         "expected": {
#             "status_code": 200
#         }}
# ]
#
#
# @pytest.fixture(params=param_test)
# def param_trans(request):
#     return request.param
#
#
# def test_baidu_search(param_trans):
#     requests.request('get', 'https://www.baidu.com', data=param_trans['payload'], headers=param_trans['headers'],
#                      params=param_trans['querystring'])


param_test1 = [{
    "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
    "contend": {
    }
},
    {
        "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        "contend": {
            # "group_id": "111",
            "group_name": "apple",
            "order": 1,
            "tag": [{
                "name": "redapple",
                "order": 1
            },
                {
                    "name": "greenapple",
                    "order": 2
                }
            ]
        }
    },
    # {
    #     "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
    #     "contend": {
    #         "id": "TAG_ID",
    #         "name": "banana",
    #         "order": 1
    #     }
    # },
    # {
    #     "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
    #     "contend": {
    #         "tag_id": [
    #             "TAG_ID_1",
    #             "TAG_ID_2"
    #          ],
    #         "group_id": [
    #             "GROUP_ID_1",
    #             "GROUP_ID_2"
    #         ]
    #     }
    # }
]


# @pytest.fixture()
# def get_token():
#     t = requests.get(
#         'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec0'
#         'c1629ebe40f45&corpsecret=lK-JtaaAb-Y5A7Aw1s7AM6eVgzvmXW1c3zGxwTWLbYE')
#     own = t.json()['access_token']
#     # print(own)
#     assert t.json()['errcode'] == 0
#     return own
#
#
# @pytest.fixture(params=param_test1)
# def params_weixin(request):
#     return request.param
#
#
# def test_find(params_weixin, get_token):
#     print(get_token)
#     r = requests.request('post', url=params_weixin['url'], params={"access_token": get_token},
#     json=params_weixin['contend'])
#     print(r.json())


def test_gettoken():
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
            "params": {"access_token": test_gettoken()}
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
                "access_token": test_gettoken()
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
            "params": {"access_token": test_gettoken()},
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
            "params": {"access_token": test_gettoken(), 'debug': 1},
            "json": {
                "tag_id": [TestWeixin.test_find(self)['tag_group'][0]['tag'][0]['id']]
            }
        }
        r = requests.request(**data)
        print(r.json())
        # assert r.json()['errmsg'] == 'ok'
        # print(r.json())
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
