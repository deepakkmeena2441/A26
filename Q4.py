from threading import *
import threading

def print_all_even_number():
        for i  in range(1,101):
            if i%2==0:
                print(i,end=" ")
        print()      
def print_all_odd_number():
        for i in range(1,101):
            if i%2!=0:
                print(i,end=" ")
        print()

t1=threading.Thread(target=print_all_even_number)
t2=threading.Thread(target=print_all_odd_number)
t1.start()
t2.start()
t1.join()
t2.join()
        