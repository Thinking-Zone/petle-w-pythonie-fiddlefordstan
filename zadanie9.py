# Pętla iterująca po liczbach od 1 do 100
for i in range(1, 101):
    if i % 7 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 7
        print(f"Pierwsza liczba podzielna przez 7 to: {i}")
        break  # Zatrzymujemy pętlę po znalezieniu pierwszej liczby podzielnej przez 7
