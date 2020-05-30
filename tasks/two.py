from .utils import shuffle_string, remove_punctuation, dump_args

# Second Task:

""" This function randomly reorders all the letters in a world."""

""" At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:"""

"""Then we again need a function that randomly reorders all the letters in a word: """

""" After that we can apply it to a sentence:"""

""" And finally get back the punctuation by changing all the words in the original text:"""


@dump_args
def second_task(s : str) -> str:
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')

    List_of_Words = remove_punctuation(s).split()
    List_of_Scrumbled_Words = []
    for elements in List_of_Words:
        shuffle_element=shuffle_string(elements)
        if len(elements) > 1:            
            while shuffle_element == elements:
                shuffle_element=shuffle_string(elements)
        List_of_Scrumbled_Words.append(shuffle_element)
    elements = len(List_of_Words)
    i = 0
    while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
    return final_string
