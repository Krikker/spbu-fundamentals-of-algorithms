class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder_tree_walk(root):
            """Complexity O(n), n = # of nodes"""
            if root is None:
                return
            inorder_tree_walk(root.left)
            nodes.append(root)
            inorder_tree_walk(root.right)

        def build_balanced_tree(left_i, right_i):
            if left_i > right_i:
                return None
            mid_i = (left_i + right_i) // 2
            root = nodes[mid_i]
            root.left = build_balanced_tree(left_i, mid_i - 1)
            root.right = build_balanced_tree(mid_i + 1, right_i)
            return root

        # This call will collect keys in nodes in the sorted order
        inorder_tree_walk(root)
        # This call will bisect over the sorted array to build a balanced tree
        return build_balanced_tree(0, len(nodes) - 1)


if __name__ == "__main__":
    # Let's solve Balance a Binary Search Tree problem:
    # https://leetcode.com/problems/balance-a-binary-search-tree

    #    root = TreeNode(val=1)
    #    root.right = TreeNode(val=2)
    #    root.right.right = TreeNode(val=3)
    #    root.right.right.right = TreeNode(val=4)
    #    balanced_root = Solution().balanceBST(root)
    #    print()

    root = TreeNode(val=2)
    root.right = TreeNode(val=5)
    root.right.right = TreeNode(val=7)
    root.right.right.left = TreeNode(val=6)
    root.right.right.left.left = TreeNode(val=5)
    root.right.right.right = TreeNode(val=8)
    balanced_root = Solution().balanceBST(root)
    print()
