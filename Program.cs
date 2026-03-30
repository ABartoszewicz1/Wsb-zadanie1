using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Wybierz opcję:");
        Console.WriteLine("1 - Kalkulator");
        Console.WriteLine("2 - Konwerter temperatur");
        Console.WriteLine("3 - Średnia ocen");

        int wybor = int.Parse(Console.ReadLine());

        if (wybor == 1)
        {
            // Kalkulator
            Console.WriteLine("Podaj pierwszą liczbę:");
            double a = double.Parse(Console.ReadLine());
            Console.WriteLine("Podaj drugą liczbę:");
            double b = double.Parse(Console.ReadLine());
            Console.WriteLine("Podaj znak działania (+, -, *, /):");
            string znak = Console.ReadLine();

            double wynik = 0;
            bool poprawne = true;

            if (znak == "+")
            {
                wynik = a + b;
            }
            else if (znak == "-")
            {
                wynik = a - b;
            }
            else if (znak == "*")
            {
                wynik = a * b;
            }
            else if (znak == "/")
            {
                if (b == 0)
                {
                    Console.WriteLine("Nie można dzielić przez zero!");
                    poprawne = false;
                }
                else
                {
                    wynik = a / b;
                }
            }
            else
            {
                Console.WriteLine("Nieprawidłowy znak działania!");
                poprawne = false;
            }

            if (poprawne)
            {
                Console.WriteLine("Wynik: " + wynik);
            }
        }
        else if (wybor == 2)
        {
            // Konwerter temperatur
            Console.WriteLine("Podaj jednostkę (C dla Celsjusza, F dla Fahrenheita):");
            string jednostka = Console.ReadLine().ToUpper();
            Console.WriteLine("Podaj temperaturę:");
            double temp = double.Parse(Console.ReadLine());

            double wynik = 0;

            if (jednostka == "C")
            {
                wynik = temp * 1.8 + 32;
                Console.WriteLine("Temperatura w Fahrenheitach: " + wynik);
            }
            else if (jednostka == "F")
            {
                wynik = (temp - 32) / 1.8;
                Console.WriteLine("Temperatura w Celsjuszach: " + wynik);
            }
            else
            {
                Console.WriteLine("Nieprawidłowa jednostka!");
            }
        }
        else if (wybor == 3)
        {
            // Średnia ocen
            Console.WriteLine("Ile ocen chcesz wpisać?");
            int n = int.Parse(Console.ReadLine());

            double suma = 0;

            for (int i = 0; i < n; i++)
            {
                Console.WriteLine("Podaj ocenę " + (i + 1) + " (1-6):");
                int ocena = int.Parse(Console.ReadLine());
                suma += ocena;
            }

            double srednia = suma / n;
            Console.WriteLine("Średnia: " + srednia.ToString("F2"));

            if (srednia >= 3)
            {
                Console.WriteLine("Uczeń zdał");
            }
            else
            {
                Console.WriteLine("Uczeń nie zdał");
            }
        }
        else
        {
            Console.WriteLine("Nieprawidłowy wybór!");
        }
    }
}