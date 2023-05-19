from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


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

    def search(self, key: Any) -> Optional[Element]:
        """Complexity: O(n)"""
        x = self.head
        while (x is not None) and (x.key != key):
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
