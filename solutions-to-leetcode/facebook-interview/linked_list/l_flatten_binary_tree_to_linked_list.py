"""
Flatten Binary Tree to Linked List
https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/322/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        pass


def main():
    input1 = TreeNode(1)
    input1.left = TreeNode(2)
    input1.left.left = TreeNode(3)
    input1.left.right = TreeNode(4)
    input1.right = TreeNode(5)
    input1.right.right = TreeNode(6)

    print(Solution().flatten(input1,))


if __name__ == "__main__":
    main()
