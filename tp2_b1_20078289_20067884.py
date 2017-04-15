from HashTable import HashTable
from Corrector import Corrector
import timing


def read_dict():
    fr = open("dict.txt", 'r')
    dictio = HashTable(len(fr.readlines()))
    fr.seek(0)
    # hashtable contenant l'alphabet pour eviter d'avoir deux fois la meme lettre
    alphabet = HashTable(256)           # le nombre de caracteres ASCII
    for word in fr:
        word = word.strip()
        dictio[word] = word
        for letter in word:
            alphabet[letter] = letter
    fr.close()
    return dictio, alphabet


def read_input():
    fr = open("input.txt", 'r')
    for ligne in fr:
        ligne = ligne.strip()
        if ligne:                        # ne corrige pas les lignes vides
            yield ligne
    fr.close()


dictio, alphabet = read_dict()

# ajouter les signes de ponctuations dans le dictionnaire pour pouvoir les conserver
for punctuation in ('.', ',', ':', ';', '!', '?', "'", '"', ' '):
    dictio[punctuation] = punctuation

corrector = Corrector(dictio, alphabet)
for ligne in read_input():
    print(corrector.correct(ligne))