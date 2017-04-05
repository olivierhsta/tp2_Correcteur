from HashTable import HashTable
from Corrector import Corrector
import timing
import os

def read_dict():
    fr = open("dict.txt", 'r')
    # parmi les langues les plus courantes dans le monde, le croate est celle dont la longueur des mots
    # est la plus courte en moyenne (environ 7 caracteres).
    # os.stat("dict.txt").st_size retourne le nombre de bits (aka nombre de caracteres) dans le fichier.
    # En divisant, par 6, on couvre toutes les langues puisque le dictionnaire
    # aura une longueur environ egale a 1/6 des caracteres du fichier ( * 2 dans __init__() de HashTable.py)
    dictionary = HashTable(os.stat("dict.txt").st_size // 6)
    for line in fr:
        line = line.strip()
        dictionary[line] = line
    fr.close()
    return dictionary


def read_input():
    fr = open("input.txt", 'r')
    for line in fr:
        line = line.strip()
        if line:                        # ne corrige pas les lignes vides
            yield line
    fr.close()

dictionary = read_dict()
corrector = Corrector(dictionary)

for line in read_input():
    print(corrector.correct(line))
