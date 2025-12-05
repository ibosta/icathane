// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        // string password = "1234";
        // while(true){
        //     Console.WriteLine("Bana sifreni ver : ");
        //     password = Console.ReadLine();
            
        //     if(password == "1234"){
        //         Console.WriteLine("Sifre dogru");
        //         break;
        //     }
        //     else{
        //         Console.WriteLine("Sifre yanlis");
        //     }
        
        
        // int gun = 7;
        
        // switch(gun){
        //     case 1:
        //       Console.WriteLine("pazartesi");
        //       break;
        //     case 2:
        //       Console.WriteLine("sali");
        //       break;
        //     case 3:
        //       Console.WriteLine("carsamba");
        //       break;
        //     case 4:
        //       Console.WriteLine("persembe");
        //       break;
        //     case 5:
        //       Console.WriteLine("cuma");
        //       break;
        //     case 6:
        //       Console.WriteLine("cumartesi");
        //       break;
        //     case 7:
        //       Console.WriteLine("pazar");
        //       break;
        // }
        
        
        int i = 0;
        int j = 0;
        while(i<4){
            j = 0;
            while(j<4){
                Console.Write("*");
                j++;
            }
            Console.WriteLine();
            i++;
        }
      
        
        
        
        
        
        
        
        
        
        
        
    }
}
