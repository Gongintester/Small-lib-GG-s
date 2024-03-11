a = 1; b = True; c = 4500 #R�ne ci�g typ c++

q,w,e = 2, False, "Textshit" #Ci�g logiczny zapis

x = y = z = 1 # To samo wszysko

dlugastring = "to\
jest\
wielo\
liniowy\
string"

betterdlugastring = """to
jest
wielo
liniowy
string"""

x = x + 1 
# lub
y += 1

print(e[4])  #Odwo�ywanie si� do index lecz
print(e[-1]) #Odwo�ywanie si� do ostatniego indexa kiedy kolwiek
print(e[:])  #Normalne s�owo
print(e[1:]) #Normalne s�owo z wyj�tkiem 
print(e[1:3])#Normalne s�owo z wywaleniem ostatnich bo 3 i od 1 

######################################################################

print(2^2)   #To nie podt�gowanie to czy parzysta
print(2**3)  #Pot�gowanie

######################################################################

if True == True:
    print(True)
elif True == True:
    print(True)
else:
    print(True)
    
######################################################################

'''
and <-> i
or  <-> lub
not <-> nie
'''

######################################################################

listaNige = {
        ("Ad", )
        ("AdSmall", )
        ("Adnig", )
    }

######################################################################

liczby = [1, 2, 3, 4, 5, 6]

#Wolniejszy i większy sposób na wykonanie for
potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

#Lepszy ładniejszy sposób na wykonanie loopa for
Newlist = [elemeent ** 2 for elemeent in liczby]

Newlist = [elemeent ** 2 
           for elemeent in liczby]

Newlist2 = [elemeent
           for elemeent in liczby
           if (elemeent % 2 == 0)
           ]

######################################################################
names = ("Imie", "BImie", "CImie", "DImie", "EImie")

namesLenght = {
    name : len(name)    
    for name in names
    if name.startswith("I")
    if name.__len__ > 3
    }