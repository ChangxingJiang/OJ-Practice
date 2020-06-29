from toolkit import TreeNode, build_TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0

            slope_left, sum_left = helper(node.left)
            slope_right, sum_right = helper(node.right)

            slope_node = abs(sum_left - sum_right)
            sum_node = sum_left + sum_right + node.val
            slope_total = slope_left + slope_right + slope_node

            return slope_total, sum_node

        return helper(root)[0]


if __name__ == "__main__":
    print(Solution().findTilt(build_TreeNode([1, 2, 3])))  # 1
