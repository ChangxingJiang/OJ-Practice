from toolkit import TreeNode, build_TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        now_node = [root]
        while now_node:
            next_node = []
            for node in now_node:
                if node.val != val:
                    return False
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            now_node = next_node
        return True


if __name__ == "__main__":
    tree = build_TreeNode([1, 1, 1, 1, 1, None, 1])
    print(Solution().isUnivalTree(tree))  # True
    tree = build_TreeNode([2, 2, 2, 5, 2])
    print(Solution().isUnivalTree(tree))  # False
