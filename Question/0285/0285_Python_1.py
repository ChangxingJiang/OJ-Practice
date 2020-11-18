from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None

        return self.find([], root, p)

    def find(self, path, node, p):
        if node.val < p.val:
            return self.find(path + [node], node.right, p)
        elif node.val > p.val:
            return self.find(path + [node], node.left, p)
        else:
            # 目标节点有右子节点的情况
            if node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node

            # 目标节点没有右子节点的情况
            else:
                while path and path[-1].val < node.val:
                    path.pop()
                if path:
                    return path.pop()
                else:
                    return None


if __name__ == "__main__":
    # 2
    tree = build_TreeNode([2, 1, 3])
    print(Solution().inorderSuccessor(tree, tree.left))

    # None
    tree = build_TreeNode([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().inorderSuccessor(tree, tree.right))

    # 3
    tree = build_TreeNode([2, None, 3])
    print(Solution().inorderSuccessor(tree, tree))
