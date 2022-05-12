import requests


class TestDemo:
    def setup_class(self):
        self.base_url = "http://litemall.hogwarts.ceshiren.com"

    def test_post_car(self):
        param1 = {
            "username": 'dawn',
            "password": 'wms20010112'
        }
        r = requests.post(self.base_url + "/wx/auth/login", json=param1)
        tk = r.json()['data']['token']

        header = {
            "X-Litemall-Token": tk
        }

        param2 = {
            "goodsId": 1181648,
            "number": 1,
            "productId": 892
        }
        r1 = requests.post(self.base_url + "/wx/cart/add", headers=header, json=param2)
        print(r1.text)

        assert r1.json()['errno'] == 0
        assert r1.json()['errmsg'] == "成功"
