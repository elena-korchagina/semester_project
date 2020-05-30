import string

from .utils import shuffle_string, remove_punctuation, dump_args

# Third Task:
""" Randomly reorder all the letters in words that are shorter than a given number of letters
(this given number of letters is an extra argument to the function):"""

""" At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:"""

"""Again we need a function that randomly reorders all the letters in a word: """

""" And then we apply it to the words, that are shorter than a given number of letters
(this given number of letters is an extra argument to the function):"""


def shuffle_short(sentence, n):
    def shuffle_short_words(word):
        if len(word) >= n:
            return word
        shuffle_word=shuffle_string(word)
        if len(word) > 1:
            while shuffle_word == word:
                shuffle_word=shuffle_string(word)
        return shuffle_word

    words = sentence.split(' ')
    return ' '.join(map(shuffle_short_words, words))


""" And get back the punctuation:"""


@dump_args
def third_task(s: str, n: int) -> str:
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')
    
    if not isinstance(n, int):
        raise TypeError('n must be a non-empty number')
    elif n < 1:
        raise ValueError('n must be a number > 0')
    
    List_of_Words = remove_punctuation(s).split()
    List_of_Scrumbled_Words = []
    for elements in List_of_Words:
        List_of_Scrumbled_Words.append(shuffle_short(elements, n))
    elements = len(List_of_Words)
    i = 0
    while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
    return final_string

# Todo (lena): move to tests
# test = 'Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall...'
# third_task(test, 4)
# print(third_task(test, 4))
