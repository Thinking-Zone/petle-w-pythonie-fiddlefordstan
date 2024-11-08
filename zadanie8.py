def zapytaj_o_pogode():
    liczba_nie = 0  # Licznik odpowiedzi "nie"
    
    while True:
        # Pobranie odpowiedzi od użytkownika
        odpowiedz = input("Czy pada? (Odpowiedz 'tak', 'nie' lub 'nie wiem'): ").lower()
        
        if odpowiedz == "nie":
            liczba_nie += 1  # Zwiększ liczbę odpowiedzi "nie"
            print("Odpowiedziałeś 'nie'.")
        elif odpowiedz == "tak":
            print(f"Zakończono! Odpowiedziałeś 'nie' {liczba_nie} razy.")
            break  # Zakończenie programu, gdy odpowiedź to "tak"
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("Nie rozumiem. Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")

# Uruchomienie programu
zapytaj_o_pogode()
