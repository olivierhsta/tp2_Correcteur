from HashTable import HashTable
import timing
import os

def read_dict():
    fr = open("dict.txt", 'r')
    # parmi les langages les plus courants dans le monde, le croate est celui dont la longueur des mots
    # est la plus courte en moyenne (environ 7 caracteres).  os.stat("dict.txt").st_size retourne le nombre
    # de bits (aka le nombre de caracteres) dans le fichier.  En divisant, par 6, on couvre toutes les langues avec
    # un dictionnaire de longueur environ egale a 1/6 des caracteres du fichier ( * 2 dans __init__() de HashTable.py)
    table = HashTable(os.stat("dict.txt").st_size // 7)
    print(os.stat("dict.txt").st_size // 7)
    for line in fr:
        line = line.strip()
        table[line] = line
    fr.close()
    return table

table = read_dict()
print(table)
print(len(table))
