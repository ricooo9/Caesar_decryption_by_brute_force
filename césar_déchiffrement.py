# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:28:38 2023

@author: Foulie Aymeric
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message_codé = input('Entrez votre message à décoder en minuscule : ')
mots = message_codé.split() 

def fr(message, taux_mots_min=0.3, taux_lettres_min=0.8):

    with open('liste_francais.txt', 'r') as f:
        mots_francais = set(f.read().split())
        
    mots = message.split()
    nb_mots_francais = sum([mot.lower() in mots_francais for mot in mots])
    taux_mots_francais = nb_mots_francais / len(mots)
    nb_lettres = sum([lettre.isalpha() for lettre in message])
    taux_lettres = nb_lettres / len(message)
    return taux_mots_francais >= taux_mots_min and taux_lettres >= taux_lettres_min

for clé in range(26):
    message_décodé = []
    for mot in mots:
        mot_décodé = []
        for lettre in mot:
            if not lettre in alphabet:
                mot_décodé.append(lettre)
            else:
                position = alphabet.index(lettre) + clé
                mot_décodé.append(alphabet[position % 26])
        message_décodé.append(''.join(mot_décodé)) 
    message_final = ' '.join(message_décodé).upper() 

    if fr(message_final):
        print('La clé de chiffrement est', clé)
        print('Le message décodé est :', message_final)
    
   