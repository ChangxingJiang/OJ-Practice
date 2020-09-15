from typing import List

from toolkit import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and stack[-1].val < n:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]


if __name__ == "__main__":
    # [6,3,5,None,2,0,None,None,1]
    print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
