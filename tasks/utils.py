import functools
import inspect
import random
import string

#We make adictionary of all punctuation signs.
PUNCTUATIONS = str.maketrans(dict.fromkeys(string.punctuation, ' '))

def shuffle_string(s: str) -> str:
    """
    Mixes all the letters in the given string
    
    :param s: the string to shuffle

    Examples:
        >>> shuffle_string('abc')
        'cba'
        >>> shuffle_string('abc d')
        'da bc'
        >>> shuffle_string('i like python')
        'okny tehiil p'
    """
    chars = list(s)
    random.shuffle(chars)
    return ''.join(chars)


def scrabble_word(word: str) -> str:
    """
    Randomly reorders all but the first and the last letters in a word
    
    :param word: the word to scrabble
   
   Examples:
        >>> scrabble_word('abc')
        'abc'
        >>> scrabble_word('abcdef')
        'acdebf'
        >>> scrabble_word('i like python')
        'iytkiep hl on'
    """
    if len(word) <= 3:
        return word
    else:
        first, mid, last = word[0], word[1:-1], word[-1]
        result_mid=shuffle_string(mid)
        while mid == result_mid:
            result_mid=shuffle_string(mid)
        return first + result_mid + last


def random_up(sentence):
    """
    Randomly makes some letters lower case and some upper case
    
    :param sentence: the sentence to mix case of the letters in
   
   Examples:
        >>> random_up('abc')
        'Abc'
        >>> random_up('abcdef')
        'acDeBf'
        >>> random_up('i like python')
        'i lIKE pYThOn'
    """
    return ''.join(random.choice((str.upper, str.lower))(c) for c in sentence)


def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from the given text
    
    :param text: the text to remove punctuation in

     Examples:
        >>> remove_punctuation('hi, how are you?')
        'hi how are you'
        >>> remove_punctuation('Mummy, where did you buy it?')
        'Mummy where did you buy it'
    
    """
    return text.translate(PUNCTUATIONS)


def dump_args(func):
    """
    Decorator to print function call details - parameters names and effective values.
    https://stackoverflow.com/a/6278457/552621
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str = ', '.join('{} = {!r}'.format(*item) for item in func_args.items())
        print(f'>>> {func.__qualname__}( {func_args_str} )')
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f'Raised: {e}\n')
            raise
        print(f'{result}\n')
        return result

    return wrapper

def char_counter(word: str) -> dict:
    ret_d={}
    for char in word:
       if char in ret_d:
           ret_d[char]+=1
       else:
           ret_d[char]=1
    return ret_d  
