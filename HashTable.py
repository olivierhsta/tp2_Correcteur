
class HashTable:

    _EMPTY = None

    def __init__(self, len_dict):
        self._table = [self._EMPTY] * (len_dict * 2)
        self._length = 0

    def _search_for(self, key):
        """
        rechercher une cle dans le la hashtable (linear probing)
        :param key: il n'est pas nécessaire d'avoir value puisque dans notre cas key == value en tout temps
        :return: tuple (presence, index) où presence est un boolean (true si l'element est dans la table)
                 et index est l'index de l'element ou l'index où l'element peut etre inseré
        """
        i = self._hashing(key)
        while True:
            if self._table[i] == key:
                return True, i
            elif self._table[i] is self._EMPTY:
                return False, i
            i = (i + 1) % len(self._table)

    def _hashing(self, key):
        """ Polynomial accumulation """
        index = ord(key[0])
        for char in key[1:]:
            # selon le livre de reference, choisir 39 pour la Polynomial accumulation cause peu de collision en anglais
            index = ord(char) + (39 * index)
        return index % len(self._table)

    def __len__(self):
        return self._length

    def __getitem__(self, key):
        present, index = self._search_for(key)
        if present:
            return self._table[index]
        else:
            return self._EMPTY

    def __setitem__(self, key, value):
        present, index = self._search_for(key)
        # puisqu'on ne veut jamais deux fois le meme mot dans le dictionnaire, ecrire le mot seulement
        # lorsqu'il n'est pas deja present
        if not present:
            self._table[index] = value
        self._length += 1

    def __iter__(self):
        for case in self._table:
            if case is not self._EMPTY:
                yield case

    def __str__(self):
        str_return = ''
        for word in self._table:
            str_return += str(word) + '\n'
        return str_return
