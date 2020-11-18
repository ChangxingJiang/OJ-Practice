import collections

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        now_level = collections.deque([root])
        while now_level:
            next_level = collections.deque()
            while now_level:
                node = now_level.popleft()
                if node == u:
                    if now_level:
                        return now_level.popleft()
                    else:
                        return None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            now_level = next_level
        return None


if __name__ == "__main__":
    # 5
    tree = build_TreeNode([1, 2, 3, None, 4, 5, 6])
    print(Solution().findNearestRightNode(tree, tree.left.right))

    # None
    tree = build_TreeNode([3, None, 4, 2])
    print(Solution().findNearestRightNode(tree, tree.right.left))

    # None
    tree = build_TreeNode([1])
    print(Solution().findNearestRightNode(tree, tree))

    # 2
    tree = build_TreeNode([3, 4, 2, None, None, None, 1])
    print(Solution().findNearestRightNode(tree, tree.left))
