from HashTable import HashTable
from Corrector import Corrector


def read_dict():
    fr = open("dict.txt", 'r')
    dictio = HashTable(len(fr.readlines()))
    fr.seek(0)
    for ligne in fr:
        ligne = ligne.strip()
        dictio[ligne] = ligne
    fr.close()
    return dictio


def read_input():
    fr = open("input.txt", 'r')
    for ligne in fr:
        ligne = ligne.strip()
        if ligne:                        # ne corrige pas les lignes vides
            yield ligne
    fr.close()


dictio = read_dict()

# ajouter les signes de ponctuations dans le dictionnaire pour pouvoir les concerver
for punctuation in ('.', ',', ':', ';', '!', '?', "'", '"', ' '):
    dictio[punctuation] = punctuation

corrector = Corrector(dictio)
for ligne in read_input():
    print(corrector.correct(ligne))

