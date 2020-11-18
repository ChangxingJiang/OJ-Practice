import bisect
from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.lst = []

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # 中序遍历二叉搜索树
        # O(N)
        self.inorder(root)

        # 二分查找目标值
        # O(logN)
        left = bisect.bisect_left(self.lst, target) - 1
        right = left + 1

        # 从目标值向两侧遍历寻找最接近的值
        # O(N)
        ans = []
        while len(ans) < k:
            if left >= 0 and right < len(self.lst):
                if target - self.lst[left] < self.lst[right] - target:
                    ans.append(self.lst[left])
                    left -= 1
                else:
                    ans.append(self.lst[right])
                    right += 1
            elif left >= 0:
                ans.append(self.lst[left])
                left -= 1
            elif right < len(self.lst):
                ans.append(self.lst[right])
                right += 1
            else:
                break

        return ans

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.lst.append(node.val)
            self.inorder(node.right)


if __name__ == "__main__":
    # [4,3]
    print(Solution().closestKValues(build_TreeNode([4, 2, 5, 1, 3]), 3.714286, 2))

    # [1]
    print(Solution().closestKValues(build_TreeNode([1]), 0, 1))

    # [1]
    print(Solution().closestKValues(build_TreeNode([1]), 4.428571, 1))

    # [1]
    print(Solution().closestKValues(build_TreeNode([1, None, 8]), 3, 1))
