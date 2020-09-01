from typing import List

from toolkit import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass


if __name__ == "__main__":
    # [3,9,20,None,None,15,7]
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
