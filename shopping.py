#!/usr/bin/env python3

"""Part 2 of a program to help you find the best path through
   -- the grocery store along with how much you will spend."""

__author__ = 'Brynne Mittleider'
__date__ = '4/18/2022'


def sort_list(multi_list):
    """Sorts a list by its second and third items

    Args:
        multi_list (list): list of lists of parameters for items to buy

    Returns:
        new_list (list): list after being sorted by its second and third items
    """
    new_list = multi_list
    for num in range(1, len(new_list)):
        new_index = num
        # Find when to insert
        while new_index > 0 and new_list[num][1] < new_list[new_index - 1][1]:
            new_index = new_index - 1
        keep_changing = True
        if not new_index > 0:
            keep_changing = False
        elif not new_list[num][1] == new_list[new_index - 1][1]:
            keep_changing = False
        elif new_list[num][1] % 2 == 0:
            if not new_list[num][2] > new_list[new_index - 1][2]:
                keep_changing = False
        elif not new_list[num][2] < new_list[new_index - 1][2]:
            keep_changing = False
        while keep_changing == True:
            new_index = new_index - 1
            if not new_index > 0:
                keep_changing = False
            elif not new_list[num][1] == new_list[new_index - 1][1]:
                keep_changing = False
            elif new_list[num][1] % 2 == 0:
                if not new_list[num][2] > new_list[new_index - 1][2]:
                    keep_changing = False
            elif not new_list[num][2] < new_list[new_index - 1][2]:
                keep_changing = False
        # Make the insertion
        row = new_list[num]
        new_list.pop(num)
        new_list.insert(new_index, row)
    return new_list


def convert_input_to_dict(string):
    """Converts a string of item parameters into the item's name
    -- and a list of its parameters.

    Args:
        string (str): a string of comma separated values relating
        -- to one item

    Returns:
        name (str): name of the item
        parameters_list (list): list of the item parameters
    """
    parameters_list = string.split(',')
    for count in range(len(parameters_list)):
        parameters_list[count] = parameters_list[count].strip()
    name = parameters_list[0].title()
    parameters_list.pop(0)
    # Convert second and third items to ints to make sorting easier
    parameters_list[0] = int(parameters_list[0])
    parameters_list[1] = int(parameters_list[1])
    parameters_list[2] = float(parameters_list[2])
    return name, parameters_list


def read_file(input_name):
    """Reads a file of item parameters and converts it into a dictionary.

    Args:
        input_name (str): name of the file to be read

    Returns:
        file_dict (dict): dictionary of item names and their parameters
    """
    file_dict = {}
    try:
        with open(input_name, 'r') as in_file:
            for line in in_file:
                line = line.replace('\n', '')
                key, value_list = convert_input_to_dict(line)
                file_dict[key] = value_list
    except FileNotFoundError:
        print('File did not exist ' + file_name)
    except OSError:
        print('Error reading file ' + file_name)
    return file_dict


def main():
    """Inputs names of items and prints their parameters
    -- sorted in a way that promotes shopping efficiency.

    Args:
        None

    Returns:
        None
    """
    # Make the dictionary
    file_name = input('File? ')
    print()
    grocery_dict = read_file(file_name)
    # Collect wanted items
    grocery_list = []
    move_on = False
    while move_on != True:
        response = input('Name? ')
        print()
        if response == 'done':
            move_on = True
        else:
            response = response.title()
            if not response in grocery_dict:
                print(response, 'is not at the store')
            else:
                item_list = grocery_dict[response]
                item_list.insert(0, response)
                grocery_list.append(item_list)
    # Convert input to list and sort
    grocery_list = sort_list(grocery_list)
    # Print result
    total = 0
    for item in grocery_list:
        price = item[3]
        total += price
        print('{:15} Aisle {:>2} Location {:>2} + {:6.2f} = {:6.2f}'.format(
        item[0], item[1], item[2], price, total))


if __name__ == '__main__':
    main()
