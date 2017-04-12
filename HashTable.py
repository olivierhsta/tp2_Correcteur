
class HashTable:

    _DELETED = object()
    _EMPTY = None

    def __init__(self, len_dict):
        self._table = [self._EMPTY] * (len_dict * 2)

    def _search_for(self, key):
        """
        rechercher une cle dans le la hashtable (linear probing)
        :param key: il n'est pas nécessaire d'avoir la valeur puisque dans notre cas key == value en tout temps
        :return: tuple (presence, index) où presence est un boolean (true si l'element est dans la table)
                 et index est l'index de l'element ou l'index où l'element peut etre inseré
        """
        i = self._hashing(key)
        avail = None
        while True:
            if self._table[i] == key:
                return True, i
            elif avail is None and self._table[i] is self._DELETED:
                avail = i
            elif self._table[i] is self._EMPTY:
                return (False, avail) if avail is not None else (False, i)
            i = (i + 1) % len(self._table)

    def _hashing(self, key):
        index = ord(key[0])
        for char in key[1:]:
            index = ord(char) + (39 * index)
        return index % len(self._table)

    def __len__(self):
        counter = 0
        for word in self._table:
            if word is not None:
                counter += 1
        return counter

    def __getitem__(self, key):
        present, index = self._search_for(key)
        if present:
            return self._table[index]
        else:
            return self._EMPTY

    def __setitem__(self, key, value):
        present, index = self._search_for(key)
        if not present:
            self._table[index] = value

    def __delitem__(self, key):
        present, index = self._search_for(key)
        if present:
            self._table[index] = self._DELETED

    def __iter__(self):
        for case in self._table:
            if case is not self._EMPTY and case is not self._DELETED:
                yield case

    def __str__(self):
        str_return = ''
        for word in self._table:
            str_return += str(word) + '\n'
        return str_return
