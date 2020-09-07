from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        stack = []
        node = root
        while node:
            # 处理节点同时包含左右节点的情况
            if node.left and node.right:
                stack.append(node.right)
                node.left, node.right = None, node.left

            # 处理节点只包含左节点的情况
            elif node.left:
                node.left, node.right = None, node.left

            # 处理节点既没有左节点也没有右节点的情况（取出栈顶元素左右右节点）
            elif not node.right and stack:
                node.right = stack.pop()

            node = node.right


if __name__ == "__main__":
    tree_1 = build_TreeNode([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(tree_1)
    print(tree_1)

    tree_2 = build_TreeNode([1, 2])
    Solution().flatten(tree_2)
    print(tree_2)
