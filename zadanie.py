import random

wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
num = random.randrange(1, 100)
liczba_prob = 1
while wprowadzona != num:
    if wprowadzona >= num:
        print('wprowadzona liczba była większa niż losowana')
    elif wprowadzona <= num:
        print('wprowadzona liczba była mniejsza niż losowana')
    wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
    liczba_prob = liczba_prob + 1
while wprowadzona == num:
    print(f'odgadles, twoja liczba to {num}')
    break
print(f'zajęło ci to {liczba_prob} razy')
