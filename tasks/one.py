
from .utils import remove_punctuation, scrabble_word, dump_args


@dump_args
def first_task(s : str) -> str:
    """
    Function randomly reorders all but the first and last letters of each word in a text.
    
    Parameters:
        s: the string to shuffle
    Returns:
        str: shuffled string
    Examples:
        >>> first_task('What can we do with the drunken sailor?')
        ' Waht can we do wtih the durnekn sloair?'
        >>> first_task('Because the sky is blue, it makes me cry')
        'Baceuse the sky is bule, it mkeas me cry'
      
    Raises: TypeError in case of an empty string
            ValueError in case that argument is not a string
    """

    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')

    # At first step we have to make our text free from punctuationsso that it doesn't mix up with the letters 
    
    list_of_words = remove_punctuation(s).split()
    
    #Then we reorder the letters in the words of a text, using function scrabble_word, that is possible to find in utils
    
    list_of_scrabbled_words = []
    for elements in list_of_words:
        list_of_scrabbled_words.append(scrabble_word(elements))
    elements = len(list_of_words)

    # And finally we substitute the words in the original text with the new, "scrambled" words
    
    i = 0
    final_string = ''
    while i < elements:
        final_string = s.replace(str(list_of_words[i]), str(list_of_scrabbled_words[i]), 1)
        s = final_string
        i += 1
    return final_string
