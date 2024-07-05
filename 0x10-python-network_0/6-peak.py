#!/usr/bin/python3
"""
Module to find a peak element in a list of integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of integers.
    """
    if not list_of_integers:
        return None
    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_helper(arr, low, high):
    """
    Helper function to find a peak using binary search.

    Parameters:
    arr (list): The list of integers.
    low (int): The lower index for the current subarray.
    high (int): The higher index for the current subarray.

    Returns:
    int: A peak element from the list.
    """
    mid = (low + high) // 2

    # Check if mid is a peak
    if (mid == 0 or arr[mid] >= arr[mid - 1]) and
    (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
        return arr[mid]

    # If the left neighbor is greater, the peak must be in the left half
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_helper(arr, low, mid - 1)

    # If the right neighbor is greater, the peak must be in the right half
    else:
        return find_peak_helper(arr, mid + 1, high)
