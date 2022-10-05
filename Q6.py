from threading import *
import threading
l=[]
def thread1():
    l.append(23)
    l.append(34)
def thread2():
    l.append(45)
def thread3():
    l.append(56)
def thread4():
    l.append(67)
def thread5():
    l.append(78)
t1=threading.Thread(target=thread1)
t2=threading.Thread(target=thread2)
t3=threading.Thread(target=thread3)
t4=threading.Thread(target=thread4)
t5=threading.Thread(target=thread5)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print(l)

