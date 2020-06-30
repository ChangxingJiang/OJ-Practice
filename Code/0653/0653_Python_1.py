from toolkit import TreeNode, build_TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(node):
            if not node:
                return []
            return helper(node.left) + [node.val] + helper(node.right)

        nums = helper(root)

        hashmap = []

        for n in nums:
            if k - n not in hashmap:
                hashmap.append(n)
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 9))  # True
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 28))  # False
