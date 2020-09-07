from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.idx = 0

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树并排序元素
        def recursor_get(node):
            if node:
                return recursor_get(node.left) + [node.val] + recursor_get(node.right)
            else:
                return []

        lst = recursor_get(root)
        lst.sort()

        # 中序遍历二叉树并填写有序元素
        def recursor_update(node):
            if node:
                recursor_update(node.left)
                node.val = lst[self.idx]
                self.idx += 1
                recursor_update(node.right)

        recursor_update(root)


if __name__ == "__main__":
    # [3,1,None,None,2]
    tree_1 = build_TreeNode([1, 3, None, None, 2])
    Solution().recoverTree(tree_1)
    print(tree_1)

    # [2,1,4,None,None,3]
    tree_2 = build_TreeNode([2, 1, 4, None, None, 3])
    Solution().recoverTree(tree_2)
    print(tree_2)
