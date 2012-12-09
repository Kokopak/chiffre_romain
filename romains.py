#!/usr/bin/env python
#-*- coding: utf-8-*-


def to_romain(nbr):
    ty = type(nbr)

    valeurs = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]
    conv = [("VIIII", "IX") , ("IIII", "IV"), ("XXXX", "XL"), 
            ("LXL", "XC"), ("CCCC", "CD"), ("DCD", "CM")]

    if ty == int:
        rom = ""
        if nbr >= 5000 :
            return "entrer un nombre < 5000"

        while nbr > 0 :
            for n, r in valeurs :
                if nbr >= n :
                    rom += r
                    nbr -= n
                    break
        for m, n in conv :
            if m in rom :
                rom = rom.replace(m, n)

        return rom

    else : 
        somme = 0
        for con in conv:
            if con[1] in nbr:
                nbr = nbr.replace(con[1], con[0])
        for let in nbr:
            for val in valeurs:
                if let in val:
                    somme += val[0]
        return somme


print """ Modes :
    1. Chiffre romain => nombre
    2. Nombre => chiffre romain"""

choix = input("Choix : ")

if choix == 1 :
    nbr =  raw_input("Nombre (en chiffre romain) : ")
    print "%s correspond à %d" % (nbr, to_romain(nbr))
elif choix == 2 :
    nbr =  input("Nombre : ")
    print "%d correspond à %s" % (nbr, to_romain(nbr))
