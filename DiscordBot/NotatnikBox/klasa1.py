imoina = {"arla", "Karlos", "Barbarosa", "barak"}

names = ( name.capitalize() for name in imoina if name.find("b") == 0 or name.find("B") == 0)

for name in names:
    print(name)
    

