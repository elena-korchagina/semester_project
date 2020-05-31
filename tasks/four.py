from .utils import random_up, remove_punctuation, dump_args
@dump_args


def fourth_task(s: str) -> str:
    """
    Function randomly makes some letters of the words in a text upper case and some lower case
        Parameters:
        s(str): the string to modify
        Returns:
        str:string  with letters,randomly made upper case.
    
    Examples:
        >>> fourth_task('What can we do with the drunken sailor?')
        'What CAN wE do witH The DruNkeN SaILoR?'
        >>> fourth_task('Because the sky is blue, it makes me cry')
        'BECaUsE tHe SKY iS bLUe, IT MakeS ME Cry'
      
    Raises: TypeError in case of an empty string
            ValueError in case that argument is not a string
    
    """
    
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')

# At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:
   
    List_of_Words = remove_punctuation(s).split()
   
# Then we work on making some letters upper case and some lower case:
    
    List_of_Scrumbled_Words = []
    for elements in List_of_Words:
        List_of_Scrumbled_Words.append(random_up(elements))
    
# Finally we replace the words in the original text with the scrambled words, so that punctuation keeps on it's places:

    elements = len(List_of_Words)
    i = 0
    while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
    return final_string
