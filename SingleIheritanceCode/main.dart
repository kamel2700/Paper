import 'dart:io';
 
class Bird{    
      var b = 2;
   }    
      // Inherits the super class  
class Parrot extends Bird{    
         //child class function  
         var a = 1;           
}  
void main() {  
      // Creating object of the child class  
      var arr = new List(1000000);
      for (var i =0; i < 1000000; i++){
      	arr[i] = new Parrot();
      }
}  