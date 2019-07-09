
"""
Description:
Author:qxy
Date: 2019-07-09 14:21
File: Multithreading 
"""

from time import ctime, sleep
import threading


def music(func):
    for i in range(2):
        print("I was listening to %s! %s" % (func, ctime()))
        print(sleep(1))


def movie(func):
    for i in range(2):
        print("I was at the %s! %s" %(func, ctime()))
        sleep(5)


threads = []
t1 = threading.Thread(target=music, args=('爱情买卖',))
threads.append(t1)

t2 = threading.Thread(target=movie, args=('阿凡达',))
threads.append(t2)


if __name__ == '__main__':
    for i in threads:
        i.setDaemon(True)
        i.start()
    i.join()

    print("all over %s" % ctime())