import functools
import inspect
import random
import string

PUNCTUATIONS = str.maketrans(dict.fromkeys(string.punctuation))


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
    return ''.join(random.choice((str.upper, str.lower))(c) for c in sentence)


def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from the given text

    TODO (Lena): add more examples!
    Examples
        >>> remove_punctuation('sdsdasd')
        'asdsadas'
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