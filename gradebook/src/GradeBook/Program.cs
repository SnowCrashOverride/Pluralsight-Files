﻿using System;
using System.Collections.Generic;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        { 
            var book = new Book("The Ultimate Gradebook");
            book.AddGrade(89.1);
            book.AddGrade(44.5);
            book.AddGrade(99.788);
            book.AddGrade(77.5);

            var stats = book.GetStatistics();
            Console.WriteLine($"The lowest grade is {stats.Low}.");
            Console.WriteLine($"The highest grade is {stats.High}.");
            Console.WriteLine($"The average grade is {stats.Average:N1}.");
        }
    }
}