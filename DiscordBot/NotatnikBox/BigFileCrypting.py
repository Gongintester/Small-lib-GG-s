import GonginLib

file = open("big.txt", "r", encoding="UTF-8")
file_text = file.read()
fout = open("exit", "x", encoding="UTF-8")

fout.write(GonginLib.Encrypting(file_text))