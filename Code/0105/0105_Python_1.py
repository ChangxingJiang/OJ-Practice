from typing import List

from toolkit import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder:
            # 寻找当前二叉树的根节点
            val = preorder[0]
            root = TreeNode(val)

            # 寻找中序遍历中的根节点位置
            idx = inorder.index(val)

            # 处理左子树
            root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])

            # 处理右子树
            root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])

            # 返回当前树的结果
            return root


if __name__ == "__main__":
    # [3,9,20,None,None,15,7]
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
