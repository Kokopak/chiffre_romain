#!/usr/bin/env python
#-*- coding: utf-8-*-


def to_romain(nbr):
    valeurs = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]

    if nbr >= 5000 :
        return "entrer un nombre < 5000"

    rom = ""
    while nbr > 0 :
        for n, r in valeurs :
            if nbr >= n :
                rom += r
                nbr -= n
                break

    #Gère le cas des "soustractions"
    conv = [("VIIII", "IX") , ("IIII", "IV"), ("XXXX", "XL"), 
            ("LXL", "XC"), ("CCCC", "CD"), ("DCD", "CM")]

    for m, n in conv :
        if m in rom :
            rom = rom.replace(m, n)

    return rom

nbr = input("Nombre : ")
print("Chiffre romain : %s" % to_romain(nbr))
