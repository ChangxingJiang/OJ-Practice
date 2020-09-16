class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.last = None
        self.first = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node:
                # 处理左子树
                dfs(node.left)

                # 处理当前节点
                if not self.last:
                    self.first = node
                    self.last = node
                else:
                    node.left = self.last
                    node.left.right = node
                    self.last = node

                # 处理右子树
                dfs(node.right)

        if root:
            dfs(root)

            self.last.right = self.first
            self.first.left = self.last

            return self.first


if __name__ == "__main__":
    pass
