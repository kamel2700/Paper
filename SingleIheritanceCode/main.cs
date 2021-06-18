using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Parent
    {
        public int a = 1;
    }
    
    public class Son: Parent
    {
        public int b = 2;
    }
    public class Program
    {
        public static void Main(string[] args)
        {
            Son s = new Son();
            Son[] houses = new Son[1000000];
            for(int i=0;i<1000000;i++){
                houses[i] = new Son();
            }
        }
    }
}