from typing import List

from toolkit import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_idx, max_val = -1, float("-inf")
            for i, n in enumerate(nums):
                if n > max_val:
                    max_val = n
                    max_idx = i
            root = TreeNode(max_val)
            root.left = self.constructMaximumBinaryTree(nums[:max_idx])
            root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
            return root


if __name__ == "__main__":
    # [6,3,5,None,2,0,None,None,1]
    print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
