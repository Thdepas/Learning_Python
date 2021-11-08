#!/usr/bin/env python3

import random
import string
import time 

mot_de_passe = input("Quel est le mot de passe : ")

def mot_aleatoire():
    lettres = string.ascii_letters
    next =""
    res = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != next:
            print(res+next) 
            next = random.choice(lettres)
        res += next 
    return res

debut = time.time()
print(mot_aleatoire())
print("Durée : " + str(time.time() - debut) + " secondes")
