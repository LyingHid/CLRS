#!/usr/bin/python
from math import floor


class Pair():
    def __init__(self, key, value=None):
        self._key = key
        self._value = value


    def __int__(self):
        return self._key


    def __lt__(self, b):
        return int(self) < int(b)


    def __le__(self, b):
        return int(self) <= int(b)


    def __eq__(self, b):
        return int(self) == int(b)


    def __ne__(self, b):
        return int(self) != int(b)


    def __ge__(self, b):
        return int(self) >= int(b)


    def __gt__(self, b):
        return int(self) > int(b)


    def __str__(self):
        return str(self._key)


    def __repr__(self):
        # return "(" + str(self._key) + ", " + repr(self._value) + ")"
        return str(self._key)


    def __floor__(self):
        return floor(self._key)


    def key(self, k=None):
        if k:
            self._key = k
        else:
            return self._key


    def value(self, v=None):
        if v:
            self._value = v
        else:
            return self._value


if __name__ == "__main__":
    a = Pair(1)
    b = Pair(2)

    print(a, int(b), a < b, a > b, a.key(), b.value(), floor(a) + floor(b))
