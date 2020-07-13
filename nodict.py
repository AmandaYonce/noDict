#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'amanda Yoncce'


class Node():
    def __init__(self, key, value=None):
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        """
        Prints a human readable representation of its
        key/value contents when asked.
        """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """
        allows the Node class to compare itself to other Node
        Objects using the built-in == operator
        """
        if self.key == other.key:
            return True
        else:
            return False


class NoDict:
    """A program that mimics the behavior of a python dictionary"""

    def __init__(self, num_buckets=10):
        """Initializes number of buckets, default is 10"""
        self.buckets = [[] for i in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string version of the NoDict contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                         bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """
        Creates a new entry in our dictionary and stores
        the entry in a bucket.
        """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for key_value in bucket:
            if key_value == new_node:
                bucket.remove(key_value)
                break
        bucket.append(new_node)

    def get(self, key):
        """
        Accesses key value pairs.
        """
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for each in bucket:
            if each == key_val:
                return each.value
        raise KeyError(f'{key} was not found')

    def __getitem__(self, key):
        """
        mimics the use of square bracket notation to
        look up dictionary entries
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        mimics the use of square bracket notation to
        set dictionary entries
        """
        self.add(key, value)
