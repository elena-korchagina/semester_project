from .utils import shuffle_string, remove_punctuation, dump_args

@dump_args

def second_task(s : str) -> str:
    """ 
    This function randomly reorders all the letters in a world.
    
        Parameters: 
        s: the string to shuffle
        Returns:
        str: shuffled string
    Examples:
        >>> second_task('What can we do with the drunken sailor?')
        ' Tahw acn ew od hwit the unekrnd lsaoir?'
        >>> second_task('Because the sky is blue, it makes me cry')
        'eaucBes teh ysk is elbu, ti kemas em cyr'
      
    Raises: 
        TypeError in case of an empty string
        ValueError in case that argument is not a string
    """
    
    if not isinstance(s, str):
        raise TypeError('s must be a non-empty string')
    elif s == '':
        raise ValueError('s must be a non-empty string')
        
# At first step we have to make our text free from punctuations , so that it doesn't mix up with the letters:

    List_of_Words = remove_punctuation(s).split()
    
#Then we  need a function shuffle_string that randomly reorders all the letters in a word, we can find it in utils

    List_of_Scrumbled_Words = []
    for elements in List_of_Words:
        shuffle_element=shuffle_string(elements)
        
# Only for words, that are longer than one letter, we need to make shure, that letters were reordered properly

        if len(elements) > 1:            
            while shuffle_element == elements:
                shuffle_element=shuffle_string(elements)
        List_of_Scrumbled_Words.append(shuffle_element)
        
# And finally get back the punctuation by changing all the words in the original text with the new, reorganised words

    elements = len(List_of_Words)
    i = 0
    while i < elements:
        final_string = s.replace(str(List_of_Words[i]), str(List_of_Scrumbled_Words[i]), 1)
        s = final_string
        i += 1
    return final_string
