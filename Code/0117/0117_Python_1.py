class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 处理特殊情况
        if not root:
            return root

        now_node = [root]
        while now_node:
            last = None
            next_node = []
            for node in now_node:
                node.next = last
                last = node
                if node.right:
                    next_node.append(node.right)
                if node.left:
                    next_node.append(node.left)
            now_node = next_node

        return root



if __name__ == "__main__":
    pass
