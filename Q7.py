from datetime import datetime
from operator import imod
from threading import Thread
import threading
from time import *
from datetime import time
def current_time():
    for i in range(1,61):
        t = datetime.today()
        current_time = t.strftime("%H:%M:%S")
        print(current_time)
        sleep(1)
    
        
def thread2():
    print("1 minute completed")
t1=threading.Thread(target=current_time)
t2=threading.Thread(target=thread2)
t1.start()
sleep(60)
t2.start()
