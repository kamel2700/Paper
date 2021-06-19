#include <iostream>
using namespace std;

int main()
{
   int sz = 10000;

   int randArray[sz];
   for(int i=0;i<sz;i++)
      randArray[i]=rand()%1000;  //Generate number between 0 to 99
  
   int n = sizeof(randArray) / sizeof(randArray[0]);
  
    /*Here we take two parameters, the beginning of the
    array and the length n upto which we want the array to
    be sorted*/
    sort(randArray, randArray + n);
  
   return 0;
}