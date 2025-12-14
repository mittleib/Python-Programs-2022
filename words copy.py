#!/usr/bin/env python3

"""Program to autocorrect a line of text."""

__author__ = 'Brynne Mittleider'
__date__ = '4/18/2022'


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

def read_file(file_name):
    file_dict = {}
    try:
        with open(file_name, 'r') as in_file:
            for line in in_file:
                line_list = line.split('=')
                key = line_list[0]
                value = line_list[1]
                file_dict[key] = value
    except FileNotFoundError:
        print('File did not exist ' + file_name)
    except OSError:
        print('Error reading file ' + file_name)
    return file_dict


def main():
    """Takes in a file of words and prints them in different orders.

    Args:
        None

    Returns:
        None
    """
    file_name = input('File? ')
    print()
    autocorrect_bank = read_file(file_name)
    line_to_correct = input('Line? ')
    print()
    # Fix statement
    list_to_correct = line_to_correct.split()
    for index in range(len(list_to_correct)):
        word = list_to_correct[index]
        if word in autocorrect_bank.keys():
            list_to_correct[index] = autocorrect_bank[word]
    list_to_correct.join(' ')
    print(list_to_correct)


if __name__ == '__main__':
    main()
