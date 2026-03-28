def kalkulator():
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
    print("Wynik: " + str(result))

def konwerter():
    direction = input("Wybierz kierunek (C dla C->F, F dla F->C): ").upper()
    temp = float(input("Podaj temperaturę: "))
    if direction == 'C':
        f = temp * 1.8 + 32
        print(str(temp) + "°C = " + str(f) + "°F")
    elif direction == 'F':
        c = (temp - 32) / 1.8
        print(str(temp) + "°F = " + str(c) + "°C")
    else:
        print("Nieprawidłowy wybór")

def srednia():
    n = int(input("Podaj liczbę ocen: "))
    if n <= 0:
        print("Liczba ocen musi być większa od zera")
        return
    suma = 0
    for i in range(n):
        ocena = float(input("Podaj ocenę " + str(i+1) + ": "))
        suma = suma + ocena
    avg = suma / n
    print("Średnia: " + str(round(avg, 2)))
    if avg >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")

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