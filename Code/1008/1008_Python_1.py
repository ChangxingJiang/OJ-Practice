from typing import List

from toolkit import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            i = 1
            while i < len(preorder) and preorder[i] < preorder[0]:
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root


if __name__ == "__main__":
    # [8,5,10,1,7,null,12]
    print(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12]))
