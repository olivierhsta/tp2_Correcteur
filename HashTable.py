
class HashTable:

    _DELETED = object()
    _EMPTY = None

    def __init__(self, len_dict):
        self._len_dict = len_dict
        self._table = [self._EMPTY] * (len_dict * 2)

    def _is_available(self, index):
        return self._table[index] in (self._EMPTY, self._DELETED)

    def _search_for(self, key):
        i = self._hashing(key)
        avail = None
        while True:
            if self[i] == key:
                return True, self._table[i]
            elif avail is None and self[i] is self._DELETED:
                avail = i
            else:
                return (False, self[avail]) if avail is not None else (False, self[i])
            i = (i + 1) % len(self)

    def _hashing(self, key):
        index = ord(key[0])
        for char in key[1:]:
            index = ord(char) + (33 * index)
        return index % len(self)

    def __len__(self):
        return self._len_dict

    def __getitem__(self, key):
        return self._table[self._hashing(key)]

    def __setitem__(self, key, value):
        self._table[self._hashing(key)] = value

    def __del__(self, key):
        self._table[self._hashing(key)] = self._DELETED
