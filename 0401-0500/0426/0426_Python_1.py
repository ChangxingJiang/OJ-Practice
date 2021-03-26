from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.last_node = None
        self.max_node = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 处理空树的特殊情况
        if not root:
            return None

        # 查找最大值节点
        # O(logN)
        node = root
        while node:
            self.last_node = node
            node = node.right

        self.max_node = self.last_node

        # 中序遍历调整二叉树
        self.dfs(root)

        return self.max_node.right

    def dfs(self, node):

        # print("START:", node.val,
        #       "(", node.left.val if node.left else None, node.right.val if node.right else None, ")")

        # 暂存当前节点的左右子节点
        left, right = node.left, node.right

        # 处理左子节点
        if left:
            self.dfs(left)

        # 处理当前节点
        self.last_node.right = node
        node.left = self.last_node
        self.last_node = node

        # 处理右子节点
        if right and node.val != self.max_node.val:
            self.dfs(right)

        # print("END:", node.val,
        #       "(", node.left.val if node.left else None, node.right.val if node.right else None, ")")


if __name__ == "__main__":
    # [1,2,3,4,5]
    Solution().treeToDoublyList(build_TreeNode([4, 2, 5, 1, 3]))

    # [1,2,3]
    Solution().treeToDoublyList(build_TreeNode([2, 1, 3]))

    # []
    Solution().treeToDoublyList(build_TreeNode([]))

    # [1]
    Solution().treeToDoublyList(build_TreeNode([1]))
