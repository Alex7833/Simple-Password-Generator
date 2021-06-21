#!/usr/bin/env python3

import random
import string
import pyperclip

i = int(input("La taille du mot de passe : "))
password = ""
for loop in range(i):
    random_choice = [random.choice(string.ascii_letters), random.choice(string.digits), random.choice(string.punctuation)]
    random_number = random.randint(0,2)
    str_pass = random_choice[random_number]
    password += str_pass
print("Votre mot de passe : \n" + password + "\n")

string = input("Voulez vous copier le mot de passe au press-papier ? (Y/n):").upper()
if string == "Y" or string == "":
    pyperclip.copy(password)
    print("Copié !\nFin")
else: 
    print("Fin")
    exit()
