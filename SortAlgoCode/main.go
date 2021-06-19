package main

import (
    "fmt"
    "math/rand"
    "time"
    "sort"
)

func main() {
    //Provide seed
    rand.Seed(time.Now().Unix())
    var x = rand.Perm(10000)
   
    sort.Ints(x)
    

    //Generate a random array of length n
    fmt.Println(x[0])
    
}