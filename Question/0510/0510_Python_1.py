# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            now = node.val
            while node.parent:
                node = node.parent
                if node.val > now:
                    return node
                elif node.right and node.right.val > now:
                    node = node.right
                    while node.left:
                        node = node.left
                    return node
        return None


if __name__ == "__main__":
    pass
