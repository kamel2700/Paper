//Rextester.Program.Main is the entry point for your code. Don't change it.
//Microsoft (R) Visual C# Compiler version 2.9.0.63208 (958f2354)

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<int> tag = GetUniqueRandomNumbers_From_1_to_10000();
            tag.Sort();
        }
        private static Random StaticRandom = new Random();

        public static List<int> GetUniqueRandomNumbers_From_1_to_10000()
        {
            return Enumerable.Range(1, 10000).OrderBy(_ => StaticRandom.Next()).ToList();
        }

            }
}