import requests

host= "http://www.cfcc.cc/"

class Com():
    def token(self,user="15011530850", psw="123456"):
        '''登录获取token  '''
        login_url = host+"app/login/oriloginapp"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "device":"003076DA-04E8-46B9-ACE6-0905EF47AC77",
            "dpmd5time":"5cfa383d4d1117553ea16f08f03ddf33",
            "dptime":"1569717755.059667",
            "login_tag":"1",
            "now_version":"5.1.3",
            "per_terminal": "1",
            "turnversion": "A",
            "user_phone": user,
            "login_pw": psw}
        r = requests.post(login_url, headers=headers, params=data)
        print(r.json())
        try:
            return_token = r.json()['data']['datavalue']['token']
        except:
            return_token = ''
        return return_token


