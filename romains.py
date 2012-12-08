#!/usr/bin/env python
#-*- coding: utf-8-*-


def to_romain(nbr):
    val_rom = list("IVXLCDM")
    val_chif = [1, 5, 10, 50, 100, 500, 1000]

    valeurs = dict(zip(val_chif, val_rom))

    lis_val = []

    if nbr < 5000 :
        ok = True
        while ok:
            try :
                val = max((x for x in val_chif if x <= nbr))
                lis_val.append(valeurs[val])
                nbr -= val
            except ValueError:
                ok = False

        chif_rom = "".join(lis_val)

        #Gère le cas des "soustractions"
        if "VIIII" in chif_rom:
            chif_rom = chif_rom.replace("VIIII", "IX")
        if "IIII" in chif_rom:
            chif_rom = chif_rom.replace("IIII", "IV")
        if "XXXX" in chif_rom:
            chif_rom = chif_rom.replace("XXXX", "XL")
        if "LXL" in chif_rom:
            chif_rom = chif_rom.replace("LXL", "XC")
        if "CCCC" in chif_rom:
            chif_rom = chif_rom.replace("CCCC", "CD")
        if "DCD" in chif_rom:
            chif_rom = chif_rom.replace("DCD", "CM")
        return chif_rom

    else :
        return "Conversion impossible !"


nbr = input("Nombre : ")

print("Chiffre romain : %s" % to_romain(nbr))
