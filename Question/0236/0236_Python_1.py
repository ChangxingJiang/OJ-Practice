from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursor(node):
            # 处理当前节点不存在的情况
            if not node:
                return False, False

            left = recursor(node.left)
            right = recursor(node.right)

            find_p = any([left[0], right[0], node.val == p.val])
            find_q = any([left[1], right[1], node.val == q.val])

            if find_p and find_q and not self.ans:
                self.ans = node

            return find_p, find_q

        recursor(root)

        return self.ans


if __name__ == "__main__":
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 3
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))  # 5
