class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None

        # 深度优先搜索构造忽略随机指针的二叉树和哈希字典
        # O(N)
        ans = NodeCopy(root.val)
        self.dfs1(root, ans)

        # 深度优先搜索构造随机指针
        # O(N)
        self.dfs2(root, ans)

        return ans

    def dfs1(self, node, copy):
        self.hashmap[node] = copy
        if node.left:
            copy.left = NodeCopy(node.left.val)
            self.dfs1(node.left, copy.left)
        if node.right:
            copy.right = NodeCopy(node.right.val)
            self.dfs1(node.right, copy.right)

    def dfs2(self, node, copy):
        if node.random:
            copy.random = self.hashmap[node.random]
        if node.left:
            self.dfs2(node.left, copy.left)
        if node.right:
            self.dfs2(node.right, copy.right)


if __name__ == "__main__":
    pass
