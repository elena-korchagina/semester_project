from .utils import random_up, remove_punctuation, dump_args

# Fourth Task:


"""This function """

""" At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:"""

""" Then we work on making some letters upper case and some lower case:"""
""" And getting back the punctuation signs:"""


@dump_args
def fourth_task(s: str) -> str:
    """
    randomly makes some letters upper case and some lower case
    :param s: the string to modify....
    """
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')

    List_of_Words = remove_punctuation(s).split()
    List_of_Scrumbled_Words = []
    for elements in List_of_Words:
        List_of_Scrumbled_Words.append(random_up(elements))
    elements = len(List_of_Words)
    i = 0
    while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
    return final_string
