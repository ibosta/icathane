using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
    int para = 100;
    
    while(true)
    {
        Console.WriteLine("Simsek McQueen Bankasina Hosgeldiniz");
        Console.WriteLine("Bakiye: "+ para +" TL");
        Console.WriteLine("1 - Para cek");
        Console.WriteLine("2 - Para yatir");
        Console.WriteLine("3 - Kart iade");
        
        int secim = Convert.ToInt32(Console.ReadLine());
        
        if(secim == 1)
        {
        Console.WriteLine("Cekilecek Miktar Giriniz");
        int cekmiktar = Convert.ToInt32(Console.ReadLine());
        
        if(cekmiktar <= para)
        {
            para = para - cekmiktar;
            Console.WriteLine("Paraniz Veriliyor");
        }
        else
        {
            Console.WriteLine("Bakiye Yetersiz");
        }
        }
        else if(secim==2)
        {
            Console.WriteLine("Yatirilacak Miktar Giriniz");
            int yatirmiktar = Convert.ToInt32(Console.ReadLine());
            para = para + yatirmiktar;
            Console.WriteLine("Paraniz Basariyla Yatirilmistir");
        }
        else if(secim == 3)
        {
            Console.WriteLine("Kartiniz Iade Ediliyor");
            break;
        }
    }
    }
}