from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Hashable

import yaml


HashFunction = Callable[[Hashable], int]


class DirectAddressTable:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


@dataclass
class ChainedHashTableElement:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


class ChainedHashTable:
    """
    It uses a linked list to avoid collision
    """

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


if __name__ == "__main__":
    # Let's consider a couple of implementations of hash tables
    with open("practicum_7/hash_table_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
