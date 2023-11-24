#!/usr/bin/python3
"""
Define a function that detrermine the fewest number of coins that meet the total
"""



def makeChange(coins, total):
    """ 
    finds the fewest coins needed for the total amound
    Args :
        coins (list)
        total (int)
    Return :
        fewest_number = none
    """

    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    fewest_number = 0
    remain_total = total
    for coin in coins:
        if remain_total == 0: return fewest_number
        if coin == remain_total:
            fewest_number = fewest_number + 1
        elif coin < remain_total:
            fewest_number = fewest_number + (remain_total // coin)
            remain_total = remain_total - (coin * fewest_number)
        else: continue
            
    if remain_total > 0: return -1
    return fewest_number
