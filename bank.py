#!/usr/bin/env python3

"""Module to compute the balance of a bank account."""

__author__ = 'Brynne Mittleider'
__date__ = '2/13/2022'

import transactions

# Bank account balance
balance = 0.0

def prompt_transaction():
    print('Balance: $' + str(balance))
    type = input('Type? ')
    print()
    while type != 'x':
        if type == 'd':
            transact('deposit')
        elif type == 'w':
            transact('withdraw')
        elif type == 'i':
            transact('interest')
        else:
            type = input('Type? ')
            print()
        print('Balance: $' + str(balance))
        type = input('Type? ')
        print()

def transact(type):
    value = float(input('Value? '))
    print()
    if type == 'deposit':
        balance = transactions.deposit(value, balance)
    elif type == 'withdraw':
        balance = transactions.withdraw(value, balance)
    elif type == 'interest':
        balance = transactions.interest(value, balance)

def main():
    """Calculate bank account balance.

    Args:
        None

    Returns:
        None
    """
    prompt_transaction()

if __name__ == '__main__':
    main()
