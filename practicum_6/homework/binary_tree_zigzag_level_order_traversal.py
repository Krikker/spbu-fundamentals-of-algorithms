from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from collections import deque

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[list[Any]]:
        if not self.root:
            return []

        levels = []
        q = deque()
        q.append(self.root)
        reverse = False

        while q:
            level_size = len(q)
            level = []

            for i in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.key)

            if reverse:
                level = level[::-1]

            reverse = not reverse
            levels.append(level)

        return levels

    def build_tree(self, list_view: list[Any]) -> BinaryTree:
        bt = BinaryTree()

        if not list_view:
            return bt

        nodes = [None if val is None else Node(val) for val in list_view]
        children = nodes[::-1]

        bt.root = children.pop()

        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()

        return bt


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = BinaryTree().build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
