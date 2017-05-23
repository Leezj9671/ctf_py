intab='abcdefghijklmnopqrstuvwxyz'

#ciphertext为原始字符串
ciphertext = 'neq{etlydsf}'
for i in range(0,25):
    trans = i + 1
    #outtab构建对应位
    outtab = ''.join([chr(((ord(i)+trans)-97)%26+97) for i in intab])
    #transtab就是解密表
    transtab = str.maketrans(intab,outtab)
    print(ciphertext.translate(transtab))

# #128位
# lstr="""U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7Y
#     H]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[
#     S#!gU#*dK9\."""  
# for p in range(127):  
#     str1 = '' 
#     for i in lstr:  
#         temp = chr((ord(i)+p)%127)  
#         if 32<ord(temp)<127 :  
#             str1 = str1 + temp   
#             feel = 1 
#         else:
#             feel = 0  
#             break 
#     if feel == 1:
#         print(str1)
