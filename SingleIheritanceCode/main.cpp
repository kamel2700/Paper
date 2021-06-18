// C++ program to demonstrate implementation
// of Inheritance
  
#include <bits/stdc++.h>
using namespace std;
 
//Base class
class Parent
{
    public:
      int id_p = 7;
};
  
// Sub class inheriting from Base Class(Parent)
class Child : public Parent
{
    public:
      int id_c = 91;
};
 
//main function
int main()
   {
      
        Child obj1;
        vector<Child> myVector;
    for(int i=0; i < 1000000; i++){
        myVector.insert(myVector.end(),Child());
    }
    
          
       
     
         
        return 0;
   }