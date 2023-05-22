# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:11:13 2023
Modified on Mon Apr  5 08:25:25 2023
@author: Foulie Aymeric
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message_codé = []

message = input('Entrez votre message à coder en minuscule : ')
clé = int(input("Entrez votre clé de cryptage : "))

for lettre in message :
    if lettre not in alphabet :
        message_codé.append(lettre)
    else :
        position = (alphabet.index(lettre) + clé) % 26
        message_codé.append(alphabet[position])
    
message_codé = ''.join(message_codé)
print("Le message codé est : ", message_codé)
