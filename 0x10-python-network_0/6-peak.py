#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers, start=None, end=None):
    """Return a peak in a list of unsorted integers."""
    if start is None:
        start = 0
    if end is None:
        end = len(list_of_integers) - 1

    if start > end:
        return None

    mid = start + (end - start) // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers, start, mid - 1)
    else:
        return find_peak(list_of_integers, mid + 1, end)
