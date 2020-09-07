from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def recursor(node, stack, _sum):
            if node:
                stack.append(node.val)  # 记录当前路径
                _sum += node.val  # 计算当前路径和

                if not node.left and not node.right:
                    if _sum == sum:
                        self.ans.append(stack)
                else:
                    if node.left:
                        recursor(node.left, stack.copy(), _sum)
                    if node.right:
                        recursor(node.right, stack.copy(), _sum)

        recursor(root, [], 0)
        return self.ans


if __name__ == "__main__":
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    print(Solution().pathSum(build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))
