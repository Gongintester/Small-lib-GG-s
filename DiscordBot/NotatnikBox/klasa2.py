
ListNie5Tak7 = ( numbersr for numbersr in range(100, 471) if (numbersr%7 == 0) and (numbersr%5 != 0)) # Moja versja to not(numbersr%5 == 0))

print(ListNie5Tak7)
for Number in ListNie5Tak7:
    print(Number)
