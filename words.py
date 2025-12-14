#!/usr/bin/env python3

"""Program to calculate the frequency of each word."""

__author__ = 'Brynne Mittleider'
__date__ = '4/17/2022'


def print_bank(bank, form):
    """Prints dictionary in a variety of ways.

    Args:
        bank (dict): word bank to print
        form (str): describes how bank should be printed

    Returns:
        None
    """
    if form == 'same':
        for key, value in bank.items():
            print(key, value)
    elif form == 'alphabetical':
        key_list = list(bank.keys())
        key_list.sort()
        for key in key_list:
            print(key, bank[key])
    elif form == 'descending':
        bank_list = list(bank.items())
        bank_list.sort(key = lambda item: item[1], reverse = True)
        for key, value in bank_list:
            print(value, key)


def main():
    """Takes in a file of words and prints them in different orders.

    Args:
        None

    Returns:
        None
    """
    file_name = input('File? ')
    print()
    word_bank = {}
    with open(file_name, 'r') as in_file:
        for line in in_file:
            line = line.replace('\n', '')
            line_list = line.split()
            for word in line_list:
                word = word.lower()
                if word in word_bank:
                    word_bank[word] += 1
                else:
                    word_bank[word] = 1
    print('Words in alphabetic order:')
    print_bank(word_bank, 'alphabetical')
    print()
    print('Words in descending frequency:')
    print_bank(word_bank, 'descending')


if __name__ == '__main__':
    main()
