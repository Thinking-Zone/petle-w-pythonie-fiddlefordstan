# Wczytujemy liczbę całkowitą od użytkownika
n = int(input("Podaj liczbę n: "))

# Sprawdzamy, czy n jest mniejsze niż 2
if n < 2:
    print("Brak liczb parzystych")
else:
    # Pętla, która iteruje po liczbach od 2 do n
    for i in range(2, n + 1, 2):
        print(i)
