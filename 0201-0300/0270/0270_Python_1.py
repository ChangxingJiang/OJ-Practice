from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        smaller, bigger = float("-inf"), float("inf")
        while root:
            if root.val < target:
                smaller = root.val
                root = root.right
            elif target < root.val:
                bigger = root.val
                root = root.left
            else:
                return int(target)

        if bigger - target > target - smaller:
            return smaller
        else:
            return bigger


if __name__ == "__main__":
    # 4
    print(Solution().closestValue(build_TreeNode([4, 2, 5, 1, 3]), 3.714286))

    # 1
    print(Solution().closestValue(build_TreeNode([1]), 4.428571))
