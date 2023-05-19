from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    next: Element = None
    prev: Element = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        x = self.head
        node_keys = []
        while x is not None:
            node_keys.append(str(x.key))
            x = x.next
        return " <-> ".join(node_keys)

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Optional[Element]:
        """Complexity: O(n)"""
        x = self.head
        while (x is not None) and (x.key != k.key):
            x = x.next
        return x

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.prev = x.prev

    @staticmethod
    def is_tail(x):
        return x.next is None


def read_from_str(s: str) -> DoublyLinkedList:
    l = DoublyLinkedList()
    for digit in list(s):
        l.insert(Element(key=int(digit)))
    return l


def jump_and_return_value(x: Optional[Element]) -> tuple[Optional[Element], int]:
    if x is None:
        return None, 0
    else:
        val = x.key
        return x.next, val


def add_two_numbers(l1: DoublyLinkedList, l2: DoublyLinkedList) -> DoublyLinkedList:
    l_sum = DoublyLinkedList()
    x_sum = l_sum.head

    x1 = l1.head
    x2 = l2.head
    residual = 0
    while (x1 is not None) or (x2 is not None):
        x1, x1_val = jump_and_return_value(x1)
        x2, x2_val = jump_and_return_value(x2)
        sum_ = residual + x1_val + x2_val
        if sum_ >= 10:
            sum_ -= 10
            residual = 1
        else:
            residual = 0
        if x_sum is None:
            x_sum = Element(key=sum_)
            l_sum.head = x_sum
        else:
            x_sum.next = Element(key=sum_)
            x_sum = x_sum.next

    if residual != 0:
        x_sum.next = Element(key=residual)
    return l_sum


if __name__ == "__main__":
    # Let's solve Add Two Numbers problem from leetcode.com:
    # https://leetcode.com/problems/add-two-numbers/description/

    # l = DoublyLinkedList()
    # l.insert(Element(key=1))
    # l.insert(Element(key=2))
    # l.insert(Element(key=3))
    # l.insert(Element(key=4))
    # e = l.search(Element(key=3))
    # l.remove(e)

    with open("practicum_6/add_two_numbers_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for c in cases:
        l1 = read_from_str(c["input"]["a"])
        l2 = read_from_str(c["input"]["b"])
        l_sum_true = read_from_str(c["output"])
        l_sum = add_two_numbers(l1, l2)
        print(
            f"Input: a = {c['input']['a']}, b = {c['input']['b']}. "
            f"Output: {l_sum}. "
            f"Expected output: {l_sum_true}"
        )
