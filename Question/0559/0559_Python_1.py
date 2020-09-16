from toolkit import Node, build_Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(node):
            if not node:
                return 0
            if not node.children:
                return 1
            maximum = 0
            for child in node.children:
                maximum = max(maximum, helper(child))
            return maximum + 1

        return helper(root)


if __name__ == "__main__":
    print(Solution().maxDepth(build_Node([1, None, 3, 2, 4, None, 5, 6])))  # 3
