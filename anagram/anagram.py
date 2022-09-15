"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word = []                     # to store a word to the dictionary in the list
start = 1                     # this is click



def main():
    """
    TODO:
    This programs  needs to find the anagrams in the dictionay and to calculate the time
    """

    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print("Welcome to StanCode 'Anagram Generator'(or -1 to quit)")
    read_dictionary()
    while True:
        s = input("Find angrams for:")
        if s == EXIT:
            break
        find_anagrams(s)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')
    #






def read_dictionary():
    """
    This programs reads dictionary by a line and we need to extend to list
    """
    global word,new_combine_word
    with open(FILE,'r')as f:
        for line in f:
            line_ = line.split()
            word.extend(line_)




def find_anagrams(s):
    """
    :param s:
    :return:
    """
    # We need to use helper to help us to find the answer
    ans = []
    find_anagranms_helper(s,[],ans)
    print(ans)

def find_anagranms_helper(s,new_combine_word,total_word):
    str = ''
    # We need to start the click
    global start
    if start:
        print('Search...')
        start = 0
    if len(new_combine_word) == len(s):
        # it is a single_word we need to put it together
        new_new_combine_word = str.join(new_combine_word)
        # To show the word in dictionary and the word not appear in total word
        if new_new_combine_word in word and new_new_combine_word not in total_word:
            # We need to print signal word
            print('Found',new_new_combine_word)
            # We need to print words that in the list
            total_word.append(new_new_combine_word)
            # to close the click
            start = 1

    else:
        # to use prefix condition to minus the search times
        if has_prefix(str.join(new_combine_word)):
            # for ever char for our input string
            for char in s:
                #  the char in word can be appear one time or one more times
                if char in new_combine_word and new_combine_word.count(char) == s.count(char):
                    pass
                else:
                    # choose
                    new_combine_word.append(char)
                    # explore
                    find_anagranms_helper(s,new_combine_word,total_word)
                    #un-choose
                    new_combine_word.pop()





def has_prefix(sub_s):
    """

#     :param sub_s:
#     :return:
#     """
#
    # We need to reduce search times
    for i in word:
        if i.startswith(sub_s):
            return True
    return False
# #

if __name__ == '__main__':
    main()
