import random

# Funkcja losująca, czy pada, czy nie
def losuj_pogode():
    return random.choice(['Pada', 'Nie pada'])

# Główna część programu
def zapytaj_o_pogode():
    odpowiedz = losuj_pogode()  # Losowanie pogody

    while True:  # Dopóki użytkownik nie zgadnie
        # Pobranie odpowiedzi od użytkownika
        odpowiedz_uzytkownika = input("Czy pada? (Podaj 'Pada' lub 'Nie pada'): ")

        # Sprawdzenie, czy odpowiedź użytkownika jest poprawna
        if odpowiedz_uzytkownika == odpowiedz:
            print("Brawo! Zgadłeś/aś poprawnie!")
            break  # Zakończenie pętli, ponieważ użytkownik zgadł poprawnie
        else:
            print("Nie zgadłeś/aś. Spróbuj ponownie.")

# Uruchomienie programu
zapytaj_o_pogode()
