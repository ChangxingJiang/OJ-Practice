from typing import List

from toolkit import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int], left=None, right=None) -> TreeNode:
        if left is None:
            left = 0
        if right is None:
            right = len(nums) - 1

        # 处理只有一个节点的情况
        if left > right:
            return None

        elif left == right:
            return TreeNode(nums[left])

        # 处理有更多节点的情况
        else:
            mid = (left + right) // 2
            head = TreeNode(nums[mid])
            head.left = self.sortedArrayToBST(nums, left=left, right=mid - 1)
            head.right = self.sortedArrayToBST(nums, left=mid + 1, right=right)
            return head


if __name__ == "__main__":
    #           0
    #          / \
    #        -3   9
    #        /   / 
    #      -10  5
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
