from typing import List

from toolkit import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recursor(i_left, i_right, p_left, p_right):
            if i_left < i_right and p_left < p_right:
                # 寻找当前二叉树的根节点
                val = postorder[p_right - 1]
                root = TreeNode(val)

                # 寻找中序遍历中的根节点位置
                idx = inorder.index(val) - i_left

                # 处理左子树
                root.left = recursor(i_left, i_left + idx, p_left, p_left + idx)

                # 处理右子树
                root.right = recursor(i_left + idx + 1, i_right, p_left + idx, p_right - 1)

                # 返回当前树的结果
                return root

        return recursor(0, len(inorder), 0, len(postorder))


if __name__ == "__main__":
    # [3,9,20,None,None,15,7]
    print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
