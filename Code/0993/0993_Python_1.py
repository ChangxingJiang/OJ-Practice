from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.depth = None
        self.father = None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def helper(node, depth=0, father=None):
            if node:
                if node.val == x or node.val == y:
                    if self.depth is None:
                        self.depth = depth + 1
                        self.father = father
                    else:
                        if self.depth == depth + 1 and self.father != father:
                            return True
                        else:
                            return False
                return helper(node.left, depth + 1, node.val) or helper(node.right, depth + 1, node.val)

        return helper(root)


if __name__ == "__main__":
    print(Solution().isCousins(build_TreeNode([1, 2, 3, 4]), 4, 3))  # False
    print(Solution().isCousins(build_TreeNode([1, 2, 3, None, 4, None, 5]), 5, 4))  # True
    print(Solution().isCousins(build_TreeNode([1, 2, 3, None, 4]), 2, 3))  # False
