#!/usr/bin/env python

import sys
import random

MAX_CHAR = 139

def get_next_word(chain, index):
    # retrieves neighboring word
    if (index < len(chain)):
        next_word = chain[index]
    else:
        # next word is None if there is no neighbor
        next_word = None

    return next_word

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # declare empty dictionary
    chain_dict = {}

    # split text string on whitespace to get a list of words
    chain_list = corpus.split()

    # iterate through list and create dictionary
    for i in range(len(chain_list)-1):
        # create a tuple_key 
        tuple_key = (chain_list[i], chain_list[i+1])

        # get next word in sequence
        next_word = get_next_word(chain_list, i + 2)

        # search for the tuple_key inside the dictionary
        if chain_dict.get(tuple_key):
            chain_dict[tuple_key].append(next_word)
        else:
            # insert the tuple_key and set frequency to 1
            chain_dict[tuple_key] = [next_word]

    return chain_dict

def concat_str(str1, str2):
    # if the first word doesn't end in a punctuation mark or the length of both words does not exceed
    # the maximum character count, concatenate
    if len(str1) + len(str2) < MAX_CHAR and str1[-1] not in ['?', '.', '!']:
        str1 += " " + str2
        return str1

    return str1

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # empty string that will later return the random text
    ret_str = " "

    # Use a word that starts with a capitalized letter as the beginning of sentence
    random_tuple = random.choice(chains.keys())
    while not random_tuple[0][0].isupper():
        random_tuple = random.choice(chains.keys())
     
    str_len = len(ret_str)
    
    while ret_str[-1] not in ['?', '.', '!'] or str_len < MAX_CHAR:
        ret_str = concat_str(ret_str, random_tuple[0])
        ret_str = concat_str(ret_str, random_tuple[1])
        
        random_value = random.choice(chains[random_tuple])
        if (random_value):
            ret_str = concat_str(ret_str, random_value)
            random_tuple = (random_tuple[1], random_value)
        else:
            break
    if ret_str[-1] not in ['?', '.', '!']:
        ret_str += "."

    return ret_str[1:]

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = '''  Would you, could you in a house
    Would you, could you with a mouse
    Would you, could you in a box
    Would you, could you with a fox
    Would you like green eggs and ham?
    Would you want them, Sam I Am?'''

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()