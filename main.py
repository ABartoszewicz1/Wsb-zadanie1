print("Wybierz opcję:")
print("1 - Kalkulator")
print("2 - Konwerter temperatur")
print("3 - Średnia ocen")

wybor = int(input())

if wybor == 1:
    # Kalkulator
    print("Podaj pierwszą liczbę:")
    a = float(input())
    print("Podaj drugą liczbę:")
    b = float(input())
    print("Podaj znak działania (+, -, *, /):")
    znak = input()

    wynik = 0
    poprawne = True

    if znak == "+":
        wynik = a + b
    elif znak == "-":
        wynik = a - b
    elif znak == "*":
        wynik = a * b
    elif znak == "/":
        if b == 0:
            print("Nie można dzielić przez zero!")
            poprawne = False
        else:
            wynik = a / b
    else:
        print("Nieprawidłowy znak działania!")
        poprawne = False

    if poprawne:
        print("Wynik: " + str(wynik))
elif wybor == 2:
    # Konwerter temperatur
    print("Podaj jednostkę (C dla Celsjusza, F dla Fahrenheita):")
    jednostka = input().upper()
    print("Podaj temperaturę:")
    temp = float(input())

    if jednostka == "C":
        wynik = temp * 1.8 + 32
        print("Temperatura w Fahrenheitach: " + str(wynik))
    elif jednostka == "F":
        wynik = (temp - 32) / 1.8
        print("Temperatura w Celsjuszach: " + str(wynik))
    else:
        print("Nieprawidłowa jednostka!")
elif wybor == 3:
    # Średnia ocen
    print("Ile ocen chcesz wpisać?")
    n = int(input())

    suma = 0

    for i in range(n):
        print("Podaj ocenę " + str(i + 1) + " (1-6):")
        ocena = int(input())
        suma += ocena

    srednia = suma / n
    print("Średnia: " + "{:.2f}".format(srednia))

    if srednia >= 3:
        print("Uczeń zdał")
    else:
        print("Uczeń nie zdał")
else:
    print("Nieprawidłowy wybór!")