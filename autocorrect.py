#!/usr/bin/env python3

"""Program to autocorrect a line of text."""

__author__ = 'Brynne Mittleider'
__date__ = '4/18/2022'


def read_file(input_name):
    """Reads a file of mispelled words and their corrected values
    -- and returns these as a dictionary.

    Args:
        input_name (str): name of the file to read

    Returns:
        file_dict (dict): dictionary of mispelled words
        -- and their corrected values
    """
    file_dict = {}
    try:
        with open(input_name, 'r') as in_file:
            for line in in_file:
                line = line.replace('\n', '')
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
    """Takes in a file of autocorrect fixes,
    -- takes in a line, and corrects the line.

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
    new_line = ' '.join(list_to_correct)
    print(new_line)


if __name__ == '__main__':
    main()
