import random

wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
losowana_liczba = random.randrange(0, 100)
print(f'wprowadziłeś liczbę: {wprowadzona}')
print(f'wylosowana liczba to {losowana_liczba}')

if wprowadzona == losowana_liczba:
    print('gratulacje odgadłeś')
else:
    print ('sprobuj ponownie')
    wprowadzona = int(input(f"podaj liczbę z zakresu 0-100: "))
# chyba musze sie nauczyć pętli
