print("Wybierz opcję:")
print("1 - kalkulator")
print("2 - konwerter temperatur")
print("3 - średnia ocen")

wybor = input("Wpisz numer: ")

if wybor == "1":
    # kalkulator
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    op = input("Podaj operację (+, -, *, /): ")
    
    if op == "+":
        wynik = num1 + num2
    elif op == "-":
        wynik = num1 - num2
    elif op == "*":
        wynik = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Nie można dzielić przez zero!")
            wynik = None
        else:
            wynik = num1 / num2
    else:
        print("Nieprawidłowa operacja!")
        wynik = None
    
    if wynik is not None:
        print(f"Wynik: {wynik}")
elif wybor == "2":
    # konwerter
    kierunek = input("Wpisz C dla Celsjusza na Fahrenheita lub F dla Fahrenheita na Celsjusza: ")
    temp = float(input("Podaj temperaturę: "))
    
    if kierunek.upper() == "C":
        f = temp * 1.8 + 32
        print(f"{temp}°C = {f}°F")
    elif kierunek.upper() == "F":
        c = (temp - 32) / 1.8
        print(f"{temp}°F = {c}°C")
    else:
        print("Nieprawidłowy wybór kierunku!")
elif wybor == "3":
    # srednia
    pass
else:
    print("Nieprawidłowy wybór")