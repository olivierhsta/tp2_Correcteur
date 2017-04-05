from HashTable import HashTable


class Corrector:

    def __init__(self, dictionary):
        self._dictionary = dictionary

    def correct(self, wrong_str):
        wrong_str = self._verify(wrong_str)
        word_list = wrong_str.split(' ')
        good_str = ''
        for word in word_list:
            try:
                self._dictionary[word.lower()]
                good_str += word + ' '
            except KeyError:
                str_replace = '[' + word  + ']' + ' ('
                for replacement in self._replace(word):
                    str_replace += replacement + ', '
                if str_replace[-2:] != ' (':
                    str_replace = str_replace[:-2] + ') '
                else:
                    str_replace += ') '
                good_str += str_replace
        return good_str

    def _verify(self, sentence):
        sentence = list(sentence)
        punctuation = ('.', ',', ':', ';', '!', '?', "'", '"', ' ')
        for i in range(len(sentence)):
            if sentence[i] in punctuation:
                if i == 0 or i == len(sentence) -1:
                    sentence[i] = ''
                elif sentence[i-1] in punctuation\
                        or sentence[i+1] in punctuation:
                    sentence[i] = ''
                else:
                    sentence[i] = ' '
        return ''.join(sentence)

    def _replace(self, word):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        table_replacement = HashTable(54 * len(word) - 2)           # 54n-2 represente la maximum de remplacement possible pour un mot de longueur n

        for i in range(len(word)):
            try:
                new_word = (word[:i] + word[i+1] + word[i] + word[i+2:]).lower()
                self._dictionary[new_word]
                table_replacement[new_word] = new_word
            except (KeyError, IndexError):
                pass

            if len(word) > 1:
                try:
                    new_word = (word[:i] + word[i+1:]).lower()
                    self._dictionary[new_word]
                    table_replacement[new_word] = new_word
                except KeyError:
                    pass
                try:
                    left_word = word[:i].lower()
                    right_word = word[i:].lower()
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
                    joined_word = ''.join(word).lower()
                    self._dictionary[joined_word.lower()]
                    table_replacement[joined_word] = joined_word
                except KeyError:
                    pass
                word_by_char[i] = temp
                temp = word
                try:
                    new_word = (word[:i] + letter + word[i:]).lower()
                    self._dictionary[new_word]
                    table_replacement[new_word] = new_word
                except KeyError:
                    pass
                word = temp
        return table_replacement
