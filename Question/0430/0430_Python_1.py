from toolkit import ListNode


class Node(ListNode):
    def __init__(self, val, prev, next, child):
        super().__init__(val)
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 处理特殊情况
        if not head:
            return head

        # 迭代深度优先搜索
        ans = node = Node(0, None, head, None)
        stack = [head]

        while stack:
            curr = stack.pop()

            node.next = curr
            curr.prev = node

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            node = curr

        ans.next.prev = None
        return ans.next


if __name__ == "__main__":
    pass
