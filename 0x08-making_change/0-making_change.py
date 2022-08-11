#!/usr/bin/python3
"""Defines the function makeChange."""


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total.
    Parameteres:
        - coins: a  list of values of coins in your possession
        - total: given amount to meet.
    """
    if total <= 0:
        return 0
    if coins is None:
        return -1

    for coin in sorted(coins, reverse=True):
        for cn in sorted(coins, reverse=True):
            sum_ = coin
            count = 1
            while sum_ <= total + 1:
                if sum_ == total:
                    return count
                sum_ += cn
                count += 1
    return -1
