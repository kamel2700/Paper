package main

import (
    "fmt"
)

func main() {



    go func(msg string) {
        for i := 0; i < 1000; i++ {
        fmt.Println(msg, ":", i)
        
        }
    }("main thread")
    
    go func(msg string) {
        for i := 0; i < 1000; i++ {
        fmt.Println(msg, ":", i)
        
        }
    }("child 2 thread")
    
    go func(msg string) {
        for i := 0; i < 1000; i++ {
        fmt.Println(msg, ":", i)
        
        }
    }("child 3 thread")
    
    
    for i := 0; i < 1000; i++ {
        fmt.Println("child thread", ":", i)
      
        }
    

    
 
}