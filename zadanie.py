import random

wprowadzona = input(f"podaj liczbę z zakresu 0-100: ")
num = random.randrange(0, 5)
liczba_prob = 1
while wprowadzona != num:
    print('try again')
    wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
    liczba_prob = liczba_prob + 1
while wprowadzona == num:
    print(f'odgadles, twoja liczba to {num}')
    break
print(f'zajęło ci to {liczba_prob} razy')
