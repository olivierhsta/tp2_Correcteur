from HashTable import HashTable


class Corrector:

    def __init__(self, dictionary):
        self._dictionary = dictionary

    def correct(self, wrong_str):
        wrong_str = self._verify(wrong_str.lower())
        word_list = wrong_str.split(' ')
        good_str = ''
        for word in word_list:
            try:
                self._dictionary[word]
                good_str += word + ' '
            except KeyError:
                str_replace = word + ' ('
                for replacement in self._replace(word):
                    str_replace += replacement + ', '
                if str_replace[-2:] != ' (':
                    str_replace = str_replace[:-2] + ') '
                else:
                    str_replace += ') '
                good_str += str_replace
        return good_str

    def _verify(self, wrong_str):
        wrong_str = list(wrong_str)
        punctuation = ('.', ',', ':', ';', '!', '?', "'", '"', ' ')
        for i in range(len(wrong_str)):
            if wrong_str[i] in punctuation:
                if i == 0 or i == len(wrong_str) -1:
                    wrong_str[i] = ''
                elif wrong_str[i-1] in punctuation\
                        or wrong_str[i+1] in punctuation:
                    wrong_str[i] = ''
                else:
                    wrong_str[i] = ' '
        return ''.join(wrong_str)

    def _replace(self, word):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        table_replacement = HashTable(54 * len(word) - 2)           # 54n-2 represente la maximum de remplacement possible pour un mot de longueur n

        for i in range(len(word)):
            try:
                new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
                self._dictionary[new_word]
                table_replacement[new_word] = new_word
            except (KeyError, IndexError):
                pass

            if len(word) > 1:
                try:
                    new_word = word[:i] + word[i+1:]
                    self._dictionary[new_word]
                    table_replacement[new_word] = new_word
                except KeyError:
                    pass
                try:
                    left_word = word[:i]
                    right_word = word[i:]
                    if len(left_word) > 0 and len(right_word) > 0:
                        self._dictionary[left_word]
                        self._dictionary[right_word]
                        table_replacement[left_word + ' ' + right_word] = left_word + ' ' + right_word
                except KeyError:
                    pass
            word_by_char = list(word)
            for letter in alphabet:
                temp = word_by_char[i]
                word_by_char[i] = letter
                try:
                    joined_word = ''.join(word)
                    self._dictionary[joined_word]
                    table_replacement[joined_word] = joined_word
                except KeyError:
                    pass
                word_by_char[i] = temp
                temp = word
                try:
                    new_word = word[:i] + letter + word[i:]
                    self._dictionary[new_word]
                    table_replacement[new_word] = new_word
                except KeyError:
                    pass
                word = temp
        return table_replacement
