import string
from .utils import shuffle_string, remove_punctuation, dump_args
@dump_args


def shuffle_short(sentence:str, n:int) -> str:
    """
    Helping function that randomly reorders all the letters in words that are shorter than a given number of letters
   
    Parameters:
    sentence(str): the string to shuffle
    n(int): the number of letters
    
    Returns:
    str: string with reordered letters
    
    Examples:
        >>> shuffle_short('What can we do with the drunken sailor')
        ' What can we do with teh drunken sailor'
        >>> shuffle_short('Because the sky is blue it makes me cry')
        'Because the syk si blue it makes me yrc'
    """
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


def third_task(s: str, n: int) -> str:
    """ 
    Randomly reorder all the letters in words that are shorter than a given number of letters
(this given number of letters is an extra argument to the function):
    :param s: the string to shuffle
    :param n: the number of letters
    Examples:
        >>> third_task('What can we do with the drunken sailor?')
        ' What can we do with teh drunken sailor?'
        >>> third_task('Because the sky is blue, it makes me cry')
        'Because the syk si blue, it makes me yrc'
    
    Raises: TypeError in case of an empty string
            ValueError in case that argument is not a string
            
            TypeError in case of an empty number
            ValueError in case that argument is not a number
    
    """
   
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')
    
    if not isinstance(n, int):
        raise TypeError('n must be a non-empty number')
    elif n < 1:
        raise ValueError('n must be a number > 0')

# At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:
   
    List_of_Words = remove_punctuation(s).split()
    
# After that we use the function shuffel_short that was described above  

    List_of_Scrumbled_Words = []
     for elements in List_of_Words:
        List_of_Scrumbled_Words.append(shuffle_short(elements, n))
        
 #Finally we replace the words in the original sentance with the scrumbled words, so that the punctuation stays on its place

        elements = len(List_of_Words)
     i = 0
     while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
     return final_string
