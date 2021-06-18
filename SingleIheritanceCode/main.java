
import java.util.*;
import java.lang.*;


import java.util.*;
import java.lang.*;

class A{  
 float a1=40000;  
}  
class B extends A{  
 int b1=10000;  
}

class Rextester{
    public static void main(String args[]){  
   B objects[]= new B[1000000];
   for (int i=0;i<1000000;i++){
       objects[i] = new B();
     
     }
}  
}