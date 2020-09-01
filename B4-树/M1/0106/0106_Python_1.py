from typing import List

from toolkit import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass


if __name__ == "__main__":
    # [3,9,20,None,None,15,7]
    print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
