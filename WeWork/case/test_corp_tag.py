import pytest
from WeWork.api.api_corp_tag import Api
from jsonpath import jsonpath


class TestCorpTag:
    def setup_class(self):
        self.case = Api()

    def test_find(self):
        r = self.case.api_find()
        # jsonpath使用
        print(jsonpath(r.json(), '$.tag_group[?(@.group_name=="标签")].tag[?(@.name == "一般")].id'))
        assert r.json()['errcode'] == 0
        # print(r.json())

    @pytest.mark.parametrize('name, order, par',
                             [['apple', '2', [{"name": "greenapple", "order": 1}, {"name": "redapple", "order": 2}]]],
                             )
    def test_add(self, name, order, par):
        r = self.case.api_add(name, order, par)
        assert r.json()['errcode'] == 0
        # print(r.json())

    @pytest.mark.parametrize('num, name', [[1, 'banana']])
    def test_edit(self, num, name):
        r = self.case.api_edit(num, name)
        assert r.json()['errcode'] == 0
        # print(r.json())

    @pytest.mark.parametrize('gnum, inum', [[1, 0]])
    def test_del(self, gnum, inum):
        r = self.case.api_del(gnum, inum)
        assert r.json()['errcode'] == 0
        # print(r.json())
