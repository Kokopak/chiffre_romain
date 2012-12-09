#!/usr/bin/env python
#-*- coding: utf-8-*-
import random

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

conv_inv= [("IX", 9) , ("IV", 4), ("XL", 40), 
        ("XC", 90), ("CD", 400), ("CM", 900)]

def to_romain(nbr):
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

def from_romain(nbr):
    somme = 0
    dic_val = {let: val for val, let in valeurs}
    for motif, valeur in conv_inv:
        if motif in nbr:
            nbr = nbr.replace(motif, "")
            somme += valeur
    for let in nbr:
        somme += dic_val[let]
    return somme

def test() :
    for nb in range(1,5000) :
        test = from_romain(to_romain(nb))
        if nb != test :
            print nb, test, to_romain(nb)

nbr =  raw_input("Entrée : ")
try :
    nbr = int(nbr)
except ValueError :
    print "%s correspond à %d" % (nbr, from_romain(nbr))
else :
    print "%d correspond à %s" % (nbr, to_romain(nbr))
