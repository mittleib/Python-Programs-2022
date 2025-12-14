#!/usr/bin/env python3

"""Module to compute types of transactions."""

__author__ = 'Brynne Mittleider'
__date__ = '2/13/2022'

def deposit(amount, balance):
    """Adds an amount to the balance.
    Args:
        amount (float): amount of money to be added
        balance (float): total money balance
    Returns:
        balance (float): total money balance
    """
    return balance + amount

def withdraw(amount, balance):
    """Removes an amount from the balance.
    Args:
        amount (float): amount of money to be removed
        balance (float): total money balance
    Returns:
        balance (float): total money balance
    """
    return balance - amount

def interest(rate, balance):
    """Applies interest to the balance.
    Args:
        rate (float): percentage of interest to be applied
        balance (float): total money balance
    Returns:
        balance (float): total money balance
    """
    dec_rate = rate / 100
    return balance * dec_rate
