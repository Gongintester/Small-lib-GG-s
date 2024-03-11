'''

Napisz program, ktory doda 3 parzyste liczby dodatnie podane przez uzytkownika

'''

inputUser = 0
LastInput = 0
x = 0 

while inputUser < 3:
    try:
        LastInput = int(input("Podaj liczbe: "))
        if not LastInput % 2 and LastInput > 0:
            print("liczba poprawna")
            x += LastInput
            inputUser += 1
        else:
            print("Nie poprawna liczba")
            continue
    except :
        print("Nie podales liczby")
        continue

print(x)
