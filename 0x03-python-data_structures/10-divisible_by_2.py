#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    div = []
    for i in  len(my_list) - 1:
        if my_list[i] % 2 == 0:
            div.append(True)
        else:
            div.append(False)

    return div
