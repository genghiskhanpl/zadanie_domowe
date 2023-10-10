import random, sys

while True:
    name = str(input('Wprowadź nazwę użytkownika: '))
    if len(name) < 3:
        print('wprowadz imię, minimum 3 znaki')
        sys.exit('konczenie programu')
    else:
        print(f'witaj {name}! Zobaczymy jak Ci pójdzie')

    wprowadzona = int(input(f"{name} podaj liczbę z zakresu 0-100: "))
    num = random.randrange(1, 2)
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
    # czesc ktora pyta czy zagramy jeszcze raz
    # instrukcje warunkowe, a to trzeba zrobic jako pętle
    while True:
        gramy_ponownie = str(input("czy gramy jeszcze raz? (t/n)?"))
        if gramy_ponownie == 't':
            print('dobra zagrajmy jeszcze raz')
            break
        elif gramy_ponownie == 'n':
            print('ok, na razie !')
            sys.exit()
        else:
            print('wproadż "t" lub "n"')

