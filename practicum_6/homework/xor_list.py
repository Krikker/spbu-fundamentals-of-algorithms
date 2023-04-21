from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import ctypes
import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = None

    def next(self, prev_ptr) -> Element:
        return self.np ^ prev_ptr

    def prev(self, curr_ptr) -> Element:
        return self.np ^ curr_ptr


class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.edge: Element = None
        self.nodes = []

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        node_keys = []
        curr_ptr = id(self.head)
        prev_ptr = 0
        while curr_ptr != 0:
            next_el = ctypes.cast(curr_ptr, ctypes.py_object).value
            node_keys.append(str(next_el.key))
            prev_ptr, curr_ptr = curr_ptr, next_el.np ^ prev_ptr
        return " <-> ".join(node_keys)

    def to_pylist(self) -> list[Any]:
        py_list = []
        curr_ptr = id(self.head)
        prev_ptr = 0
        while curr_ptr != 0:
            next_el = ctypes.cast(curr_ptr, ctypes.py_object).value
            py_list.append(next_el.key)
            prev_ptr, curr_ptr = curr_ptr, next_el.next(prev_ptr)
        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""
        curr_ptr = id(self.head)
        prev_ptr = 0
        while curr_ptr != 0:
            next_el = ctypes.cast(curr_ptr, ctypes.py_object).value
            if next_el.key == k:
                return next_el
            prev_ptr, curr_ptr = curr_ptr, next_el.next(prev_ptr)
        return None

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        if self.head is None:
            self.head = x
            self.edge = x
            x.np = 0
        else:
            x.np = id(self.head)
            self.head.np ^= id(x)
            self.head = x
        self.nodes.append(x)

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        curr_ptr = id(self.head)
        prev_ptr = 0
        next_el = ctypes.cast(curr_ptr, ctypes.py_object).value
        while curr_ptr != 0 and next_el.key != x.key:
            prev_ptr, curr_ptr = curr_ptr, next_el.next(prev_ptr)
            if curr_ptr != 0:
                next_el = ctypes.cast(curr_ptr, ctypes.py_object).value
        if curr_ptr != 0:
            prev_el = ctypes.cast(prev_ptr, ctypes.py_object).value
            next_after_ptr = next_el.np ^ prev_ptr
            if next_after_ptr != 0:
                next_next_el = ctypes.cast(next_after_ptr, ctypes.py_object).value
                prev_el.np = prev_el.np ^ curr_ptr ^ next_after_ptr
                next_next_el.np = next_next_el.np ^ curr_ptr ^ prev_ptr
            else:
                prev_el.np = prev_el.np ^ curr_ptr
                self.edge = prev_el
            self.nodes.remove(next_el)

    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """
        curr_ptr = id(self.head)
        prev_ptr = 0
        while curr_ptr != 0:
            next_ptr = ctypes.cast(curr_ptr, ctypes.py_object).value.np ^ prev_ptr
            ctypes.cast(curr_ptr, ctypes.py_object).value.np = prev_ptr ^ next_ptr
            prev_ptr, curr_ptr = curr_ptr, next_ptr
        self.head, self.edge = self.edge, self.head
        return self


if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev

    with open("xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
            elif op_info["op"] == "remove":
                l.remove(Element(key=op_info["key"]))
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(py_list)
        print(f"Case #{i + 1}: {py_list == c['output']}")
