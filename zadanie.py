import random, sys
gramy_ponownie = ''

while True:
    name = input('Wprowadź nazwę użytkownika: ')
    if len(name) < 3:
        print('wprowadz imię, minimum 3 znaki')
        sys.exit('konczenie programu')

    wprowadzona = int(input(f"{name} podaj liczbę z zakresu 0-100: "))
    num = random.randrange(1, 5)
    liczba_prob = 1
    while wprowadzona != num:
        if wprowadzona >= num:
            print('Wprowadzona liczba była większa niż losowana')
        elif wprowadzona <= num:
            print('Wprowadzona liczba była mniejsza niż losowana')
        wprowadzona = int(input(f'Wpisz liczbę z zakresu 0-100: '))
        liczba_prob = liczba_prob + 1
    while wprowadzona == num:
        print(f'Gratulacje {name} odgadles, Twoja liczba to {num}')
        break
    print(f'Zajęło ci to {liczba_prob} razy')
    gramy_ponownie = str(input("czy gramy jeszcze raz? (t/n)?"))

    if gramy_ponownie == 't':
        print('zagrajmy')
        continue
    elif gramy_ponownie == 'n':
        print('na razie')
        sys. exit()
    else:
        print('wpisz "t" lub "n": ')
#czesc ktora pyta czy zagramy jeszcze raz

