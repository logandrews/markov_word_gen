#!/usr/bin/python

import random

class MarkovTable(object):
    def __init__(self):
        self.count = 0
        self.dictionary = {}

    def increment(self, key):
        self.dictionary[key] = self.dictionary.setdefault(key, 0) + 1
        self.count = self.count + 1

    def get(self):
        r = random.randint(0, self.count - 1)
        s = 0
        for k, v in self.dictionary.iteritems():
            s = s + v
            if s >= r:
                return k
        return " "

    def __str__(self):
        return "({0}) {1}".format(self.count, self.dictionary)

class MarkovChain(object):
    def __init__(self):
        self.dictionary = {}

    def add(self, key, value):
        self.dictionary.setdefault(key, MarkovTable()).increment(value)

    def get(self, key):
        table = self.dictionary.get(key)
        return table.get() if table is not None else None

