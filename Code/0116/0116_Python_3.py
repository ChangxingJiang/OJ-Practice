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

        head = root
        while head.left:
            head.left.next = head.right
            node = head
            while node.next:
                node.right.next = node.next.left
                node = node.next
                node.left.next = node.right
            head = head.left

        return root


if __name__ == "__main__":
    pass
