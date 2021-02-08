import random
import string
import pyperclip

i = int(input("La taille du mot de passe : "))
cliped = ""
for loop in range(i):
    random_choice = [random.choice(string.ascii_letters), random.choice(string.digits), random.choice(string.punctuation)]
    test = random.randint(0,2)
    clip = random_choice[test]
    cliped = cliped + clip
print("Votre mot de passe : \n" + cliped + "\n")

string = input("Voulez vous copier le mot de passe au press-papier ? (Y/n):").upper()
if string == "Y" or string == "":
    pyperclip.copy(cliped)
    print("Copié !\nFIN")
else: 
    print("FIN")
    exit()
