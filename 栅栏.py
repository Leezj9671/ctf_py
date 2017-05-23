#python 3.5
#栅栏密码

e = 'rhasbenvaoylii'

elen = len(e)
field=[]
for i in range(2, elen):
    if(elen%i == 0):
        field.append(i)

for f in field:
    b = int(elen / f)
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print('分为'+str(f)+'栏时，解密结果为： '+d)