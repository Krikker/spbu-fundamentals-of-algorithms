from __future__ import annotations
from typing import Any, Optional


class TreeNode:
    def __init__(
        self,
        key: Any = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
        p: Optional[TreeNode] = None,
    ):
        self.key: Any = key
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
        self.p: Optional[TreeNode] = p  # will be used in the successor search


class BinarySearchTree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def insert(self, z: TreeNode) -> None:
        """Complexity: O(h), where h is the tree height
        Just like the search procedures,insert begins at the
        root of the tree and the pointer x traces a simple path
        downward looking for None to replace with the input item z.
        The procedure maintains the trailing pointer y as the parent
        of x. After initialization, the while loop in causes these two
        pointers to move down the tree, going left or right depending
        on the comparison of z.key with x.key, until x becomes None.
        This None occupies the position where we wish to place the
        input item z. We need the trailing pointer y, because by
        the time we find the NIL where z belongs, the search has proceeded
        one step beyond the node that needs to be changed.
        """
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u: TreeNode, v: TreeNode) -> None:
        """
        In order to move subtrees around within the binary search tree, we define a
        transplant(), which replaces one subtree as a child of its parent with
        another subtree. When transplant() replaces the subtree rooted at node u with
        the subtree rooted at node v, node u's parent becomes node v's parent, and u's
        parent ends up having v as its appropriate child.
        """
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self, z: TreeNode) -> None:
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = tree_minimum(z.right)
            if y.p is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y


def tree_search(x: TreeNode, k: Any) -> TreeNode:
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x: TreeNode, k: Any) -> TreeNode:
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x: TreeNode):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x: TreeNode):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x: TreeNode):
    """
    If all keys are distinct, the successor of a node x
    is the node with the smallest key greater than x.key.
    """
    if x.right is not None:
        return tree_minimum(x.right)
    # If the right subtree of node x is empty
    # and x has a successor y, then y is
    # the lowest ancestor of x whose left child
    # is also an ancestor of x
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


if __name__ == "__main__":
    # Let's implement a binary search tree tree.
    root = TreeNode(key=2)
    root.right = TreeNode(key=5, p=root)
    node_to_delete = TreeNode(key=7, p=root.right)
    root.right.right = node_to_delete
    root.right.right.left = TreeNode(key=6, p=root.right.right)
    root.right.right.left.left = TreeNode(key=5, p=root.right.right.left)
    root.right.right.right = TreeNode(key=8, p=root.right.right)
    found_x = iterative_tree_search(x=root, k=7)
    min_x = tree_minimum(x=root)
    max_x = tree_maximum(x=root)
    print()

    bst = BinarySearchTree(root)
    bst.insert(TreeNode(key=30))
    bst.delete(node_to_delete)
    print()
#    for i in range(1, len(commands)):
#        command = commands[i]
#        arg_list = args[i]
#        if command == "put":
#            returned_values.append(lru_cache.put(*arg_list))
#        if command == "get":
#            returned_values.append(lru_cache.get(*arg_list))
#    assert returned_values == [None, None, None, 1, None, -1, None, -1, 3, 4]
