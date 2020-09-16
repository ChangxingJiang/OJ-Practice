from toolkit import TreeNode, build_TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        hashmap = []

        def helper(node):
            if node:
                if (k - node.val) in hashmap:
                    return True
                hashmap.append(node.val)
                return helper(node.left) or helper(node.right)
            else:
                return False

        return helper(root)


if __name__ == "__main__":
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 9))  # True
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 28))  # False
