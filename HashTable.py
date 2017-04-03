
class HashTable:

    def __init__(self, dict_len):
        self._table = [None] * (dict_len * 2)

    def __getitem__(self, key):
        return self._table[self._hash_function(key)]

    def _hash_function(self, key):
        index = 0

        return index

    def __setitem__(self, key, value):
        self._table[self._hash_function(key)] = value

    def __del__(self, key):
        del self._table[self._hash_function(key)]
