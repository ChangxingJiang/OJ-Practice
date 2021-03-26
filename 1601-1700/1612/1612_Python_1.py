import collections


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1, count2 = collections.Counter(), collections.Counter()
        self.dfs(root1, count1)
        self.dfs(root2, count2)
        return count1 == count2

    def dfs(self, node, count):
        if node:
            if not node.left and not node.right:
                count[node.val] += 1
            else:
                self.dfs(node.left, count)
                self.dfs(node.right, count)


if __name__ == "__main__":
    pass
