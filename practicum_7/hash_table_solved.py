from __future__ import annotations
from abc import ABC, abstractmethod
from ast import Call
from dataclasses import dataclass
from typing import Any, Callable, Hashable
from collections.abc import Iterable

import numpy as np
from numpy.typing import NDArray
import networkx as nx
import yaml

from src.data_structures import DoublyLinkedList, Element


class DirectAddressTable:
    def __init__(self, key_universe_size: int, dtype: Any) -> None:
        self.table: NDArray = np.empty((key_universe_size), dtype=dtype)
        self.table.fill(None)

    def insert(self, key: int, x: Any) -> None:
        self.table[key] = x

    def search(self, key: int) -> None:
        return self.table[key]

    def remove(self, key: int) -> None:
        self.table[key] = None


HashFunction = Callable[[Hashable], int]


@dataclass
class ChainedHashTableElement:
    key: Hashable
    data: Any
    next: ChainedHashTableElement
    prev: ChainedHashTableElement


class ChainedHashTable:
    """
    It uses a linked list to avoid collision
    """

    def __init__(self, h: HashFunction, hash_table_size: int) -> None:
        self.table: NDArray = np.empty((hash_table_size), dtype=ChainedHashTableElement)
        self.table.fill(None)
        self.h = h

    def insert(self, x: Element) -> None:
        hash_value = self.h(x.key)
        if self.table[hash_value] is None:
            self.table[hash_value] = DoublyLinkedList()
        self.table[hash_value].insert(x)

    def search(self, key: Hashable) -> None:
        hash_value = self.h(key)
        if self.table[hash_value] is not None:
            return self.table[hash_value].search(key)
        return None

    def remove(self, x: Element) -> None:
        hash_value = self.h(x.key)
        if self.table[hash_value] is not None:
            self.table[hash_value].remove(x)


if __name__ == "__main__":
    # Let's consider a couple of implementations of hash tables
    with open("practicum_7/hash_table_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    # First, implement a direct-address table
    # for i, c in enumerate(cases):
    #    table = DirectAddressTable(
    #        key_universe_size=c["input"]["max_table_size"], dtype=object
    #    )
    #    for op_info in c["input"]["ops"]:
    #        if op_info["op"] == "insert":
    #            table.insert(key=op_info["key"], x=op_info["data"])
    #        elif op_info["op"] == "remove":
    #            table.remove(key=op_info["key"])
    # print()

    # Second, implement a chained hash table with the division method for creating a hash function
    for i, c in enumerate(cases):
        hash_table_size = int(c["input"]["max_table_size"] // 2)
        table = ChainedHashTable(
            h=lambda x: x % hash_table_size, hash_table_size=hash_table_size
        )
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                table.insert(Element(key=op_info["key"], data=op_info["data"]))
            elif op_info["op"] == "remove":
                e = table.search(key=op_info["key"])
                table.remove(e)
    print()

    # Third, implement a chained hash table with the multiplication method for creating a hash function:
    # h(k) = floor(m(kA - floor(kA))), where m is the hash table size and A is a magical number from 0 to 1.
    # Knuth suggests it should be A = s / 2^w and be close to (sqrt(5) - 1) / 2.
    
    # Conventionally, 
    for i, c in enumerate(cases):
        hash_table_size = int(c["input"]["max_table_size"] // 2)
        table = ChainedHashTable(
            h=lambda x: x % hash_table_size, hash_table_size=hash_table_size
        )
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                table.insert(Element(key=op_info["key"], data=op_info["data"]))
            elif op_info["op"] == "remove":
                e = table.search(key=op_info["key"])
                table.remove(e)
    print()

    # py_list = l.to_pylist()
    # print(f"Case #{i + 1}: {py_list == c['output']}")
