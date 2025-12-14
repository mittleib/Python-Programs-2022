#!/usr/bin/env python3

"""Program that could be a starting point for a Turn It In program."""

__author__ = 'Brynne Mittleider'
__date__ = '4/11/2022'

NUM_STRINGS = 2


def updateString(given_string):
    """Update a given string.

    Args:
        given_string (str): the string to have minor differences removed upon

    Returns:
        final_string (str): the final updated string
    """
    updated_string = given_string.lower()
    updated_string = updated_string.replace(',','')
    updated_string = updated_string.replace('.','')
    string_list = updated_string.split()
    final_string = '-'.join(string_list)
    return final_string


def main():
    """Accept two strings, remove minor differences, and print updated string.

    Args:
        None

    Returns:
        None
    """
    old_strings = []
    updated_strings = []
    for num in range(NUM_STRINGS):
        input_statement = 'String ' + str(num + 1) + '? '
        old_strings.append(input(input_statement))
        print()
    for string in old_strings:
        new_string = updateString(string)
        updated_strings.append(new_string)
        print(string, 'simplifies to', new_string)
    same = True
    temp_string = updated_strings[0]
    for string in updated_strings:
        if string != temp_string:
            same = False
    if same:
        print('SAME')
    else:
        print('DIFFERENT')


if __name__ == '__main__':
    main()
