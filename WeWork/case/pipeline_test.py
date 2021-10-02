import pytest
from WeWork.api.api_corp_tag import Api


class TestPipe:
    def setup_class(self):
        self.case = Api()

    @pytest.mark.smoke
    def test1(self):
        self.case.api_find()
        self.case.api_add('apple', 2, [{"name": "greenapple", "order": 1}, {"name": "redapple", "order": 2}])
        self.case.api_edit(1, 'banana')
        self.case.api_del(1, 0)
