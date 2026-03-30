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
    pass
elif wybor == "3":
    # srednia
    pass
else:
    print("Nieprawidłowy wybór")