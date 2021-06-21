//Rextester.Program.Main is the entry point for your code. Don't change it.
//Microsoft (R) Visual C# Compiler version 2.9.0.63208 (958f2354)

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading;
namespace Rextester
{
    
   class Program
   {
      public static void Main(string[] args)
      {
         // Create and start the thread
         
         Thread thread1 = new Thread(SomeTaskThatNeedsToFinish);
         thread1.Start(1);
          Thread thread2 = new Thread(SomeTaskThatNeedsToFinish);
         thread2.Start(2);
          Thread thread3 = new Thread(SomeTaskThatNeedsToFinish);
         thread3.Start(3);
          

          for (int i=0; i<1000; i++){
                Console.WriteLine(i + " :Main thread");
                
                
                
                
                    }
         // Does not proceed beyond here until thread function has finished
         thread1.Join();
          thread2.Join();
          thread3.Join();

         // Once finished your program is free to continue...
         Console.WriteLine("Task completed.  Press a key to exit.");
       
      }

      private static void SomeTaskThatNeedsToFinish(object data)
      {
         for (int i=0; i<1000; i++){
             Console.WriteLine($"{i}:Child {data} thread");
                
                
                
                
         }         
      }
   }
}