from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        node = root
        while node:
            if node.left:
                # 寻找当前右子树应移动到的位置
                now = node.left
                while now.right:
                    now = now.right

                # 移动当前右子树
                now.right = node.right

                # 修改当前节点
                node.left, node.right = None, node.left

            node = node.right


if __name__ == "__main__":
    tree_1 = build_TreeNode([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(tree_1)
    print(tree_1)

    tree_2 = build_TreeNode([1, 2])
    Solution().flatten(tree_2)
    print(tree_2)
