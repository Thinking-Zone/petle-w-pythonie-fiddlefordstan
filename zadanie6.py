# Pętla 'for' i pętla 'while' różnią się głównie w sposobie, w jaki kontrolują przepływ programu.

# Pętla 'for' jest najczęściej używana, gdy znamy dokładną liczbę iteracji z góry.
# W pętli 'for' zwykle iterujemy po określonym zbiorze danych (np. liście, zakresie liczb) lub po innych obiektach iterowalnych.
# Składnia pętli 'for' jest bardziej zwięzła, ponieważ pozwala na automatyczne kontrolowanie liczby powtórzeń.

# Przykład pętli 'for':
for i in range(1, 6):  # Zaczynamy od 1, kończymy na 5 (liczba iteracji jest znana)
    print(i)

# Pętla 'while' jest używana, gdy chcemy, aby kod powtarzał się dopóki nie zostanie spełniony jakiś warunek.
# W pętli 'while' liczba iteracji nie jest z góry znana i zależy od warunku, który może się zmieniać w trakcie działania programu.
# Pętla 'while' jest bardziej elastyczna, ale wymaga, aby programista zadbał o poprawne zakończenie pętli (np. zmianę warunku, aby pętla się zakończyła).

# Przykład pętli 'while':
i = 1
while i <= 5:  # Pętla działa dopóki zmienna 'i' jest mniejsza lub równa 5
    print(i)
    i += 1  # Zwiększamy 'i' o 1, aby pętla miała szansę zakończyć się
