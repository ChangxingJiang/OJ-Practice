from toolkit import TreeNode, build_TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def inner_helper(node, aim):
            if node is None and aim is None:
                return True
            elif node is None or aim is None:
                return False
            return node.val == aim.val and inner_helper(node.left, aim.left) and inner_helper(node.right, aim.right)

        def helper(node):
            if node:
                if node.val == t.val:
                    if inner_helper(node, t):
                        return True
                return helper(node.left) or helper(node.right)
            else:
                return False

        return helper(s)


if __name__ == "__main__":
    s1 = build_TreeNode([3, 4, 5, 1, 2])
    t1 = build_TreeNode([4, 1, 2])
    print(Solution().isSubtree(s1, t1))  # True
    s2 = build_TreeNode([3, 4, 5, 1, 2, None, None, 0, None])
    t2 = build_TreeNode([4, 1, 2])
    print(Solution().isSubtree(s2, t2))  # False
