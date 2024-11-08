# Inicjalizacja zmiennej sumującej
suma = 0

# Iterowanie po liczbach od 1 do 100
for i in range(1, 101, 2):  # krok 2, zaczynając od 1, aby wybierać liczby nieparzyste
    suma += i

# Wyświetlenie wyniku
print("Suma wszystkich liczb nieparzystych od 1 do 100 wynosi:", suma)
