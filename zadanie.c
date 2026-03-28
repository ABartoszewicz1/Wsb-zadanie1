#include <stdio.h>

int main() {
    int wybor;
    printf("Wybierz opcje:\n");
    printf("1 - Kalkulator\n");
    printf("2 - Konwerter temperatur\n");
    printf("3 - Srednia ocen\n");
    scanf("%d", &wybor);

    if (wybor == 1) {
        // Kalkulator
        double a, b, wynik;
        char znak;
        printf("Podaj pierwsza liczbe: ");
        scanf("%lf", &a);
        printf("Podaj druga liczbe: ");
        scanf("%lf", &b);
        printf("Podaj znak dzialania (+, -, *, /): ");
        scanf(" %c", &znak);

        int poprawne = 1;
        if (znak == '+') {
            wynik = a + b;
        } else if (znak == '-') {
            wynik = a - b;
        } else if (znak == '*') {
            wynik = a * b;
        } else if (znak == '/') {
            if (b == 0) {
                printf("Nie mozna dzielic przez zero!\n");
                poprawne = 0;
            } else {
                wynik = a / b;
            }
        } else {
            printf("Nieprawidlowy znak dzialania!\n");
            poprawne = 0;
        }

        if (poprawne) {
            printf("Wynik: %.2f\n", wynik);
        }
    } else if (wybor == 2) {
        // Konwerter temperatur
        char jednostka;
        double temp, wynik;
        printf("Podaj jednostke (C dla Celsjusza, F dla Fahrenheita): ");
        scanf(" %c", &jednostka);
        printf("Podaj temperature: ");
        scanf("%lf", &temp);

        if (jednostka == 'C' || jednostka == 'c') {
            wynik = temp * 1.8 + 32;
            printf("Temperatura w Fahrenheitach: %.2f\n", wynik);
        } else if (jednostka == 'F' || jednostka == 'f') {
            wynik = (temp - 32) / 1.8;
            printf("Temperatura w Celsjuszach: %.2f\n", wynik);
        } else {
            printf("Nieprawidlowa jednostka!\n");
        }
    } else if (wybor == 3) {
        // Srednia ocen
        int n;
        printf("Ile ocen chcesz wpisac? ");
        scanf("%d", &n);

        double suma = 0;
        int i;
        for (i = 0; i < n; i++) {
            int ocena;
            printf("Podaj ocene %d (1-6): ", i + 1);
            scanf("%d", &ocena);
            suma += ocena;
        }

        double srednia = suma / n;
        printf("Srednia: %.2f\n", srednia);

        if (srednia >= 3) {
            printf("Uczen zdal\n");
        } else {
            printf("Uczen nie zdal\n");
        }
    } else {
        printf("Nieprawidlowy wybor!\n");
    }

    return 0;
}