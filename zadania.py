def kalkulator():
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        op = input("Podaj operację (+, -, *, /): ")
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Błąd: dzielenie przez zero")
                return
        else:
            print("Nieprawidłowa operacja")
            return
        print(f"Wynik: {result}")
    except ValueError:
        print("Błąd: nieprawidłowe dane wejściowe")

def konwerter():
    try:
        direction = input("Wybierz kierunek (C dla C->F, F dla F->C): ").upper()
        temp = float(input("Podaj temperaturę: "))
        if direction == 'C':
            f = temp * 1.8 + 32
            print(f"{temp}°C = {f}°F")
        elif direction == 'F':
            c = (temp - 32) / 1.8
            print(f"{temp}°F = {c}°C")
        else:
            print("Nieprawidłowy wybór")
    except ValueError:
        print("Błąd: nieprawidłowe dane wejściowe")

def srednia():
    try:
        n = int(input("Podaj liczbę ocen: "))
        if n <= 0:
            print("Liczba ocen musi być większa od zera")
            return
        suma = 0
        for i in range(n):
            ocena = float(input(f"Podaj ocenę {i+1}: "))
            suma += ocena
        avg = suma / n
        print(f"Średnia: {avg:.2f}")
        if avg >= 3.0:
            print("Uczeń zdał.")
        else:
            print("Uczeń nie zdał.")
    except ValueError:
        print("Błąd: nieprawidłowe dane wejściowe")

while True:
    print("\nWybierz zadanie:")
    print("1. Kalkulator")
    print("2. Konwerter temperatur")
    print("3. Średnia ocen")
    print("0. Wyjście")
    wybor = input("Twój wybór: ")
    if wybor == '1':
        kalkulator()
    elif wybor == '2':
        konwerter()
    elif wybor == '3':
        srednia()
    elif wybor == '0':
        break
    else:
        print("Nieprawidłowy wybór")