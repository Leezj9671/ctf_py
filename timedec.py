from time import time

def UsedTimeDec(func):
    def wrapper():
        st = time()
        func()
        print('[*]Program used time: {}s'.format(time() - st))
    return wrapper