from typing import List

from toolkit import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursor(p_left, p_right, i_left, i_right):
            if p_left < p_right and i_left < i_right:
                # 寻找当前二叉树的根节点
                val = preorder[p_left]
                root = TreeNode(val)

                # 寻找中序遍历中的根节点位置
                idx = inorder.index(val) - i_left

                # 处理左子树
                root.left = recursor(p_left + 1, p_left + idx + 1, i_left, i_left + idx)

                # 处理右子树
                root.right = recursor(p_left + idx + 1, p_right, i_left + idx + 1, i_right)

                # 返回当前树的结果
                return root

        return recursor(0, len(preorder), 0, len(inorder))


if __name__ == "__main__":
    # [3,9,20,None,None,15,7]
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
