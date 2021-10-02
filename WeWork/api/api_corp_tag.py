from WeWork.api.base_api import Public


class Api(Public):
    def api_find(self):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": self.holder}
        }
        return self.send(data)

    def api_add(self, name, order, par):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            "params": {
                "access_token": self.holder
            },
            "json": {
                # "group_id": "GROUP_ID",
                "group_name": name,
                "order": order,
                "tag": par
            }
        }
        return self.send(data)

    def api_edit(self, num, name):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            "params": {"access_token": self.holder},
            "json": {
                "id": self.api_find().json()['tag_group'][num]['group_id'],
                "name": name,
                "order": 1,
            }
        }
        return self.send(data)

    def api_del(self, gnum, inum):
        data = {
            "method": 'post',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {"access_token": self.holder, 'debug': 1},
            "json": {
                "tag_id": [self.api_find().json()['tag_group'][gnum]['tag'][inum]['id']]
            }
        }
        return self.send(data)


# if __name__ == '__main__':
#     a = Api().api_find()
#     print(a.json())
