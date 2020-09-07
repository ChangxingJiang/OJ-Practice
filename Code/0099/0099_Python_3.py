from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.idx = 0
        self.x = None
        self.y = None
        self.last = None

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树并寻找顺序错误的位置
        def recursor_get(node):
            if node:
                recursor_get(node.left)
                if self.last and self.last.val >= node.val:
                    if not self.x:
                        self.x = self.last
                    self.y = node
                self.last = node
                recursor_get(node.right)

        recursor_get(root)

        # 交换两个点
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val


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
