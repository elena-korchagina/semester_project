"""
First task
"""
from .utils import remove_punctuation, scrabble_word, dump_args


@dump_args
def first_task(s : str) -> str:
    """
    Randomly reorders all but the first and last letters of each word (as in the original internet meme).
    """

    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')

    # print('first_task[in]:', s)
    # At first step we have to make our text free from punctuations
    # so that it doesn't mix up with the letters
    list_of_words = remove_punctuation(s).split()
    list_of_scrabbled_words = []
    for elements in list_of_words:
        list_of_scrabbled_words.append(scrabble_word(elements))
    elements = len(list_of_words)

    # And finally we get the punctuation back. For that we substitute the words
    # in the original text with the new, "scrambled" words
    i = 0
    final_string = ''
    while i < elements:
        final_string = s.replace(str(list_of_words[i]), str(list_of_scrabbled_words[i]), 1)
        s = final_string
        i += 1

    # print('first_task[out]:', final_string)
    return final_string
