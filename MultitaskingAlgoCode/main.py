import threading
from time import sleep

def thread1():
    """
    A function that can be used by a thread
    """
 
    for i in range(1000):
        print(i)
        #sleep(0.001) 
       
    print()
def thread3():
    """
    A function that can be used by a thread
    """
 
    for i in range(1000):
        print(i)

        
def thread4():
    """
    A function that can be used by a thread
    """
 
    for i in range(1000):
        print(i)
        
def thread2():
    """
    A function that can be used by a thread
    """

    for i in range(1000):
        print(i)
        #sleep(0.001) 
        
   
 
if __name__ == '__main__':
   
    my_thread = threading.Thread(target=thread1, args=())
    my_thread.start()
    
    my_thread = threading.Thread(target=thread2, args=())
    my_thread.start()
    
    my_thread = threading.Thread(target=thread3, args=())
    my_thread.start()
    
    my_thread = threading.Thread(target=thread4, args=())
    my_thread.start()