using System;

public class ATM
{
    public static void Main(string[] args)
    {
        int TLbakiye = 0;
        
        while(true)
        {
            Console.WriteLine("===== E-Bank ATM =====");
            Console.WriteLine(" Bakiyeniz : " + TLbakiye);
            Console.WriteLine(" 1 - Para Yatır ");
            Console.WriteLine(" 2 - Para Çek ");
            Console.WriteLine(" 3 - Çıkış Yap ");
            Console.WriteLine("======================");
            Console.Write(" ");
            int islem = Convert.ToInt32(Console.ReadLine());
            
            if(islem == 1)
            {
                Console.Write(" Yatırılacak Tutarı Giriniz : ");
                int yatirma = Convert.ToInt32(Console.ReadLine());
                
                if(yatirma <= 0)
                {
                    Console.WriteLine(" Lütfen Geçerli Bir Miktar Giriniz! ");
                }
                
                else
                {
                    TLbakiye = TLbakiye + yatirma;
                    Console.WriteLine(" Paranız Başarıyla Yatırıldı! ");
                }
            }
            
            else if(islem == 2)
            {
                Console.Write(" Çekilecek Tutarı Giriniz : ");
                int cekme = Convert.ToInt32(Console.ReadLine());
                
                if(TLbakiye >= cekme)
                {
                    TLbakiye = TLbakiye - cekme;
                    Console.WriteLine(" Paranız Başarıyla Çekildi! ");
                }
                
                else
                {
                    Console.WriteLine(" Hesabınızda Yeterli Para Yok! ");
                }
            }
            
            else if (islem == 3)
            {
                Console.WriteLine(" Hesabınızdan Başarıyla Çıkış Yapıldı! ");
                break;
            }
        }
    }
}
