import random

wprowadzona = input(f"podaj liczbę z zakresu 0-100: ")
num = random.randrange(0, 5)

while wprowadzona != num:
    print('try again')
    wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
while wprowadzona == num:
    print(f'odgadles, twoja liczba to {num}')
    break

