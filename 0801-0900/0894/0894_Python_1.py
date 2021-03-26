import copy
from typing import List

from toolkit import TreeNode


class Solution:
    def __init__(self):
        self.ans = []
        self.already = set()

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # 处理无法实现满二叉树的情况
        if N % 2 == 0:
            return []

        # 计算需要递归的深度
        n = N // 2

        # 递归生成所有满足的结果
        root = TreeNode(0)

        def recursor(leaf_lst, k):
            if k == 0:
                if (tree_str := str(root)) not in self.already:
                    self.ans.append(copy.deepcopy(root))
                    self.already.add(tree_str)
            else:
                for leaf in leaf_lst:
                    leaf.left = TreeNode(0)
                    leaf.right = TreeNode(0)
                    new_leaf_lst = leaf_lst.copy()
                    new_leaf_lst.remove(leaf)
                    new_leaf_lst.append(leaf.left)
                    new_leaf_lst.append(leaf.right)
                    recursor(new_leaf_lst, k - 1)
                    leaf.right = None
                    leaf.left = None

        recursor([root], n)

        return self.ans


if __name__ == "__main__":
    # [
    #   [0,0,0,null,null,0,0,null,null,0,0],
    #   [0,0,0,null,null,0,0,0,0],
    #   [0,0,0,0,0,0,0],
    #   [0,0,0,0,0,null,null,null,null,0,0],
    #   [0,0,0,0,0,null,null,0,0]
    # ]
    print(Solution().allPossibleFBT(7))
