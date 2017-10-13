# https://findneo.github.io/2017/10/nupt-vigenere/
# key:
# 1.明文和密文一定为可见字节，因此做异或的时候出现不可见字符则排除
# 2.XOR的特性：如果 cipher = plain ^ key，那么 plain = cipher ^ key
# 3.加密过程中密钥循环使用，加密方式为ch ^ key[i % KEY_LENGTH]
def getCipher(file='code.txt'):
    '''从文件中读取十六进制串，返回十六进制数组
    '''
    c = open(file).read()
    codeintlist = []
    codeintlist.extend((map(lambda i: int(c[i:i + 2], 16), range(0, len(c), 2))))
    return codeintlist

def getFrequency(cipher, keyPoolList):
    ''' 传入的密文作为数字列表处理
        传入密钥的字符集应为列表，依次包含各字节字符集。
            形如[[0x11,0x12],[0x22]]
        返回字频列表，依次为各字节字符集中每一字符作为密钥组成部分时对应的明文字频
            形如[{
                    0x11:{'a':2,'b':3},
                    0x12:{'e':6}
                 },
                 {
                    0x22:{'g':1}
                 }]
    '''
    freqList = []
    keyLen = len(keyPoolList)
    for i in range(keyLen):
        posFreq = dict()
        for k in keyPoolList[i]:
            posFreq[k] = dict()
            for c in cipher[i::keyLen]:
                p = chr(k ^ c)
                posFreq[k][p] = posFreq[k][p] + 1 if p in posFreq[k] else 1
        freqList.append(posFreq)
    return freqList
def calCorrelation(cpool):
    '''传入字典，形如{'e':2,'p':3}
        返回可能性，0~1,值越大可能性越大
        (correlation between the decrypted column letter frequencies and
        the relative letter frequencies for normal English text)
    '''
    frequencies = {"e": 0.12702, "t": 0.09056, "a": 0.08167, "o": 0.07507, "i": 0.06966, "n": 0.06749, "s": 0.06327, "h": 0.06094, "r": 0.05987, "d": 0.04253, "l": 0.04025, "c": 0.02782, "u": 0.02758, "m": 0.02406, "w": 0.02360, "f": 0.02228, "g": 0.02015, "y": 0.01974, "p": 0.01929, "b": 0.01492, "v": 0.00978, "k": 0.00772, "j": 0.00153, "x": 0.00150, "q": 0.00095, "z": 0.00074}
    relative = 0.0
    total = 0
    fpool = 'etaoinshrdlcumwfgypbvkjxqz'
    total = sum(cpool.values())  # 总和应包括字母和其他可见字符
    for i in cpool.keys():
        if i in fpool:
            relative += frequencies[i] * cpool[i] / total
    return relative
def analyseFrequency(cfreq):
    key = []
    for posFreq in cfreq:
        mostRelative = 0
        for keyChr in posFreq.keys():
            r = calCorrelation(posFreq[keyChr])
            if r > mostRelative:
                mostRelative = r
                keychar = keyChr
        key.append(keychar)
    return key
def vigenereDecrypt(cipher, key):
    plain = ''
    cur = 0
    ll = len(key)
    for c in cipher:
        plain += chr(c ^ key[cur])
        cur = (cur + 1) % ll
    return plain
def getKeyPool(cipher, stepSet, plainSet, keySet):

    keyPool = dict()
    for step in stepSet:
        maybe = [None] * step
        for pos in range(step):
            maybe[pos] = []
            for k in keySet:
                flag = 1
                for c in cipher[pos::step]:
                    if c ^ k not in plainSet:
                        flag = 0
                if flag:
                    maybe[pos].append(k)
        for posPool in maybe:
            if len(posPool) == 0:
                maybe = []
                break
        if len(maybe) != 0:
            keyPool[step] = maybe
    return keyPool


def main():
    pt = list(range(32,127))
    key = list(range(0xff + 1))
    klen = list(range(1, 14))
    cipher = getCipher('vig.txt')
    keyPool = getKeyPool(cipher=cipher, stepSet=klen, plainSet=pt, keySet=key)
    print(keyPool)
    for i in keyPool:
        freq = getFrequency(cipher, keyPool[i])
        key = analyseFrequency(freq)
        plain = vigenereDecrypt(cipher, key)
        print(key, plain)

if __name__ == '__main__':
    main()
    