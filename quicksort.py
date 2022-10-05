# Author: Xiaoxuan
# Date: 5/25/2021
# Purpose: randomized quicksort
from random import randint


def partition(the_list, p, r, compare_func):
    # randomize
    chosen = randint(p, r)
    temp = the_list[chosen]
    the_list[chosen] = the_list[r]
    the_list[r] = temp

    i = p - 1
    j = p
    while j <= r:
        if compare_func(the_list[j], the_list[r]):
            i += 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
            j += 1
        else:
            j += 1

    return i


def quicksort(the_list, compare_func, p=0, r=None):
    if r is None:
        r = len(the_list) - 1

    if p >= r:
        return

    q = partition(the_list, p, r, compare_func)
    quicksort(the_list, compare_func, p, q-1)
    quicksort(the_list, compare_func, q+1, r)


def sort(the_list, compare_func):
    quicksort(the_list, compare_func)
