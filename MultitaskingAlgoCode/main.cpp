#include <iostream>
#include <thread>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
 
void foo(int a)
{
    
    for (int i=0; i<1000;i++){
        std::cout << i << '\n'<< a <<"child";
       // std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
    
    
}
 
int main()
{
    
    std::thread thread(foo, 1); // foo is the function to execute, 10 is the
                               // argument to pass to it
 
    std::thread thread1(foo, 2);
    std::thread thread2(foo, 3);
    // Keep going; the thread is executed separately
 
    // Wait for the thread to finish; we stay here until it is done
    
    
    for (int i=0; i<1000;i++){
        std::cout << i << '\n' << "main";
       //std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
    
    // Create and execute the thread
     thread.join();
    thread1.join();
    thread2.join();
    
 
    return 0;
}