import random


caracteres = "+-_/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("por favor ingrese la longitud de la contraseña: "))
pasword = ""
for i in range(longitud):
    a =  random.choice(seq= caracteres)
    pasword = pasword + a
print(pasword)