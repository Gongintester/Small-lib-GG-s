liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

Newlist = [elemeent ** 2 for elemeent in liczby]