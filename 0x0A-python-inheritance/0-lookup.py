#!/usr/bin/python3
"""This module defines a function for looking up an object's attributes."""

def lookup(obj):
    """Return a list of an object's available attributes."""
    return dir(obj)
