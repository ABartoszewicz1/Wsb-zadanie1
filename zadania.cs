using System;

class Program {
    static void Main() {
        while (true) {
            Console.WriteLine("\nWybierz zadanie:");
            Console.WriteLine("1. Kalkulator");
            Console.WriteLine("2. Konwerter temperatur");
            Console.WriteLine("3. Średnia ocen");
            Console.WriteLine("0. Wyjście");
            string wybor = Console.ReadLine();
            switch (wybor) {
                case "1":
                    Kalkulator();
                    break;
                case "2":
                    Konwerter();
                    break;
                case "3":
                    Srednia();
                    break;
                case "0":
                    return;
                default:
                    Console.WriteLine("Nieprawidłowy wybór");
                    break;
            }
        }
    }

    static void Kalkulator() {
        try {
            Console.Write("Podaj pierwszą liczbę: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("Podaj drugą liczbę: ");
            double num2 = double.Parse(Console.ReadLine());
            Console.Write("Podaj operację (+, -, *, /): ");
            string op = Console.ReadLine();
            double result = 0;
            switch (op) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 != 0) {
                        result = num1 / num2;
                    } else {
                        Console.WriteLine("Błąd: dzielenie przez zero");
                        return;
                    }
                    break;
                default:
                    Console.WriteLine("Nieprawidłowa operacja");
                    return;
            }
            Console.WriteLine($"Wynik: {result}");
        } catch (FormatException) {
            Console.WriteLine("Błąd: nieprawidłowe dane wejściowe");
        }
    }

    static void Konwerter() {
        try {
            Console.Write("Wybierz kierunek (C dla C->F, F dla F->C): ");
            string direction = Console.ReadLine().ToUpper();
            Console.Write("Podaj temperaturę: ");
            double temp = double.Parse(Console.ReadLine());
            if (direction == "C") {
                double f = temp * 1.8 + 32;
                Console.WriteLine($"{temp}°C = {f}°F");
            } else if (direction == "F") {
                double c = (temp - 32) / 1.8;
                Console.WriteLine($"{temp}°F = {c}°C");
            } else {
                Console.WriteLine("Nieprawidłowy wybór");
            }
        } catch (FormatException) {
            Console.WriteLine("Błąd: nieprawidłowe dane wejściowe");
        }
    }

    static void Srednia() {
        try {
            Console.Write("Podaj liczbę ocen: ");
            int n = int.Parse(Console.ReadLine());
            if (n <= 0) {
                Console.WriteLine("Liczba ocen musi być większa od zera");
                return;
            }
            double suma = 0;
            for (int i = 0; i < n; i++) {
                Console.Write($"Podaj ocenę {i+1}: ");
                double ocena = double.Parse(Console.ReadLine());
                suma += ocena;
            }
            double avg = suma / n;
            Console.WriteLine($"Średnia: {avg:F2}");
            if (avg >= 3.0) {
                Console.WriteLine("Uczeń zdał.");
            } else {
                Console.WriteLine("Uczeń nie zdał.");
            }
        } catch (FormatException) {
            Console.WriteLine("Błąd: nieprawidłowe dane wejściowe");
        }
    }
}