from re import S
from threading import *
import threading 

def sumofnumber1():

        
        for i in range(1,51):
            s=s+i
        print(s)
def sumofnumbers2():
    
    for i in range(51,101):
        s=s+i
        print(s)

        
t1=threading.Thread(target=sumofnumber1)
t2=threading.Thread(target=sumofnumbers2)
s=0
t1.start()
t2.start()
t1.join()
t2.join()

      

