package main

import (  
    "fmt"
)

type Pet struct {
  name string
}

type Dog struct {
  Pet
  Breed string
}

func (p *Pet) Speak() string {
  return fmt.Sprintf("my name is %v", p.name)
}

func (p *Pet) Name() string {
  return p.name
}

func (d *Dog) Speak() string {
  return fmt.Sprintf("%v and I am a %v", d.Pet.Speak(), d.Breed)
}

func main() {
    x := []Dog{}
    
  
    for i := 0; i < 10000000; i++ {
         x = append(x, Dog{Pet: Pet{name: "spot"}, Breed: "pointer"})
    
    }
}