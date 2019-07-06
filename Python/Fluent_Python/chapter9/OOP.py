"""
Description:
Author:qxy
Date: 2019-07-06 18:25
File: OOP 
"""

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecpde = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecpde))
        return cls(*memv)


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)
print(v1)

v1_clone = eval(str(v1))
print(v1_clone == v1)

print(abs(v1))

print(bool(v1))