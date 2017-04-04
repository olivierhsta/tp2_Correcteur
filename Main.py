from HashTable import HashTable


def read_dict():
    fr = open("dict.txt", 'r')
    len_dict = sum(1 for line in fr if line.rstrip())           # ignore les lignes vides
    table = HashTable(len_dict)
    for line in fr:
        line = line.strip()
        table[line] = line
    fr.close()
