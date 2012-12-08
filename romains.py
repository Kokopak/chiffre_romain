#!/usr/bin/env python
#-*- coding: utf-8-*-


def to_romain(nbr):
    valeurs = {1: 'I', 100: 'C', 5: 'V', 1000: 'M', 10: 'X', 50: 'L', 500: 'D'}
    lis_val = []

    if nbr >= 5000 :
        return "entrer un nombre < 5000"

    while nbr > 0 :
        for x in sorted(valeurs.iterkeys(), reverse=True) :
            if nbr >= x :
                lis_val.append(valeurs[x])
                nbr -= x
                break
    chif_rom = "".join(lis_val)

    #Gère le cas des "soustractions"
    conv = {"VIIII": "IX", "IIII": "IV", "XXXX": "XL", 
            "LXL": "XC", "CCCC": "CD", "DCD": "CM"}

    for m in conv.iterkeys() :
        if m in chif_rom :
            chif_rom = chif_rom.replace(m, conv[m])

    return chif_rom

nbr = input("Nombre : ")
print("Chiffre romain : %s" % to_romain(nbr))
