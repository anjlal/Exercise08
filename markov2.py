#!/usr/bin/env python

import sys
import random

MAX_CHAR = 139

def get_next_word(chain, index):
    if (index < len(chain)):
        next_word = chain[index]
    else:
        # The successor word would be None if tuple_key is the last 2 words of input
        next_word = None

    return next_word

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chain_dict = {}

    chain_list = corpus.split()

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
    if len(str1) + len(str2) < MAX_CHAR and str1[-1] not in ['?', '.', '!']:
        str1 += " " + str2
        return str1

    return str1

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    ret_str = ""
    end_the_str = False

    while len(ret_str) < MAX_CHAR:
        # Use a word starts with a capitalized letter as the beginning of sentence
        random_tuple = random.choice(chains.keys())
        while not random_tuple[0][0].isupper():
            random_tuple = random.choice(chains.keys())

        while len(ret_str) < MAX_CHAR:
            if len(ret_str) + len(random_tuple[0]) > MAX_CHAR:
                end_the_str = True
                break;
            ret_str = concat_str(ret_str, random_tuple[0])
            if len(ret_str) + len(random_tuple[1]) > MAX_CHAR:
                end_the_str = True
                break;
            ret_str = concat_str(ret_str, random_tuple[1])
            
            random_value = random.choice(chains[random_tuple])
            if (random_value):
                if len(ret_str) + len(random_value) > MAX_CHAR:
                    end_the_str = True
                    break;
                ret_str = concat_str(ret_str, random_value)
                random_tuple = (random_tuple[1], random_value)
            else:
                break

        if end_the_str:
            break

    return ret_str

def make_text2(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    ret_str = " "
    # Use a word starts with a capitalized letter as the beginning of sentence
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
    random_text = make_text2(chain_dict)
    print random_text

if __name__ == "__main__":
    main()