from turtle import st
from typing import OrderedDict


def removeduplicate(str):
    return "".join(set(str))


def orderremoveduplicate(str):
    return "".join(OrderedDict.fromkeys(str))

str = "geeksforgeeks"
print(removeduplicate(str))
print(orderremoveduplicate(str))