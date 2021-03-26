from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.idx = 0

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树
        def recursor_get(node):
            if node:
                return recursor_get(node.left) + [node.val] + recursor_get(node.right)
            else:
                return []

        # 寻找需要被交换的两个节点
        lst = recursor_get(root)
        x, y = None, None
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                if not x:
                    x = lst[i]
                y = lst[i + 1]

        if x is None or y is None:
            return

        # 中序遍历二叉树并调换指定顺序
        def recursor_update(node):
            if node:
                recursor_update(node.left)

                # 调整当前值
                if node.val == x:
                    node.val = y
                elif node.val == y:
                    node.val = x

                recursor_update(node.right)

        recursor_update(root)


if __name__ == "__main__":
    # [3,1,None,None,2]
    tree_1 = build_TreeNode([1, 3, None, None, 2])
    Solution().recoverTree(tree_1)
    print(tree_1)

    # [2,1,4,None,None,3]
    tree_2 = build_TreeNode([3, 1, 4, None, None, 2])
    Solution().recoverTree(tree_2)
    print(tree_2)

    # [1,0]
    tree_2 = build_TreeNode([0, 1])
    Solution().recoverTree(tree_2)
    print(tree_2)
