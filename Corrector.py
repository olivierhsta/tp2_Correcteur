from HashTable import HashTable


class Corrector:
    def __init__(self, dictionary, alphabet):
        self._dictionary = dictionary
        self._alphabet = alphabet

    def correct(self, str_to_correct):
        str_to_correct = self._verify_pun(str_to_correct)
        word_list = str_to_correct.split(' ')
        good_str = ''
        for word in word_list:
            if word != '':
                if self._dictionary[word.lower()] is not None:
                    good_str += word + ' '
                else:
                    str_replace = '[' + word + ']' + ' ('
                    for replacement in self._replace(word):
                        str_replace += replacement + ', '
                    if str_replace[-2:] != ' (':
                        str_replace = str_replace[:-2] + ') '
                    else:
                        str_replace += ') '
                    good_str += str_replace
        return good_str

    def _verify_pun(self, sentence):
        temp_sentence = sentence
        punctuation = ('.', ',', ':', ';', '!', '?', "'", '"')
        counter = 0
        for i in range(len(sentence)):
            if sentence[i] in punctuation:
                if i == 0:
                    temp_sentence = sentence[i] + ' ' + sentence[i + 1:]
                    counter += 1
                elif i == len(sentence) - 1:
                    temp_sentence = temp_sentence[:len(temp_sentence) - 1] + ' ' + sentence[i]
                    counter += 1
                else:
                    if sentence[i + 1] == ' ' and sentence[i - 1] != ' ':
                        temp_sentence = temp_sentence[:i + counter] + ' ' + sentence[i:]
                        counter += 1
                    elif sentence[i + 1] != ' ' and sentence[i - 1] == ' ':
                        temp_sentence = temp_sentence[:i + counter] + sentence[i] + ' ' + sentence[i + 1:]
                        counter += 1
                    elif sentence[i + 1] != ' ' and sentence[i - 1] != ' ':
                        temp_sentence = temp_sentence[:i + counter] + ' ' + sentence[i] + ' ' + sentence[i + 1:]
                        counter += 2
        return temp_sentence

    def _replace(self, word):
        # hashtable pour eviter d'avoir 2x le meme mot
        table_replacement = HashTable((2 * len(self._alphabet) + 2) * len(word) +len(self._alphabet) - 2)
        # (2x+2)n + x-2 = maximum de remplacements possibles pour un mot de longueur n et un alphabet de longueur x

        for i in range(len(word)):
            # essayer d'intervertir toutes les lettres adjacentes
            try:
                new_word = (word[:i] + word[i + 1] + word[i] + word[i + 2:]).lower()
                if self._dictionary[new_word] is not None:
                    table_replacement[new_word] = new_word
            except IndexError:
                pass

            if len(word) > 1:
                # essayer de supprimer chacune des lettres du mot
                new_word = (word[:i] + word[i + 1:]).lower()
                if self._dictionary[new_word] is not None:
                    table_replacement[new_word] = new_word

                # essayer de separer le mot en deux a tous les endroits possibles
                left_word = word[:i].lower()
                right_word = word[i:].lower()
                if len(left_word) > 0 and len(right_word) > 0:
                    if self._dictionary[left_word] is not None and self._dictionary[right_word] is not None:
                        table_replacement[left_word + ' ' + right_word] = left_word + ' ' + right_word

            word_by_char = list(word)
            for letter in self._alphabet:
                # echanger une lettre avec toutes les lettres de l'alphabet
                temp = word_by_char[i]
                word_by_char[i] = letter
                joined_word = ''.join(word_by_char).lower()
                if self._dictionary[joined_word.lower()] is not None:
                    table_replacement[joined_word] = joined_word
                word_by_char[i] = temp

                # ajouter chacune des lettres de l'alphabet entre chaque lettre
                if len(word) == 1:
                    new_word = (letter + word[i]).lower()
                    if self._dictionary[new_word] is not None:
                        table_replacement[new_word] = new_word

                    new_word = (word[i] + letter).lower()
                    if self._dictionary[new_word] is not None:
                        table_replacement[new_word] = new_word
                else:
                    if i == len(word) - 1:
                        new_word = (word[:i + 1] + letter + word[i + 1:]).lower()
                        if self._dictionary[new_word] is not None:
                            table_replacement[new_word] = new_word
                    new_word = (word[:i] + letter + word[i:]).lower()
                    if self._dictionary[new_word] is not None:
                        table_replacement[new_word] = new_word

        return table_replacement
