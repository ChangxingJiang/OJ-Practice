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

        level_left_most = root  # 当前层最左侧的结点
        while True:
            next_level_left_most = None  # 下一行最左侧的节点
            last_node = None  # 当前节点左侧的节点
            node = level_left_most  # 当前层用来遍历的节点
            while node:
                if node.left:
                    if last_node:
                        last_node.next = node.left
                    if not next_level_left_most:
                        next_level_left_most = node.left
                    last_node = node.left
                if node.right:
                    if last_node:
                        last_node.next = node.right
                    if not next_level_left_most:
                        next_level_left_most = node.right
                    last_node = node.right
                node = node.next

            if next_level_left_most:
                level_left_most = next_level_left_most
            else:
                break

        return root


if __name__ == "__main__":
    pass
