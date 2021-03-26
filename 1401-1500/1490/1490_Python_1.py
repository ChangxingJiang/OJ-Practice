class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        copy = Node(root.val)
        self.dfs(root, copy)
        return copy

    def dfs(self, node, copy):
        for node_child in node.children:
            copy_child = Node(node_child.val)
            self.dfs(node_child, copy_child)
            copy.children.append(copy_child)
        

if __name__ == "__main__":
    pass
