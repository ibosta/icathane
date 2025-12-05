using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        int i = 0;
        int j = 0;
        while(i < 4)
        {
            j = 0;
            while(j < 4)
            {
                Console.Write("*  ");
                j++;
            }
            Console.WriteLine();
            i++;
        }
    }
}