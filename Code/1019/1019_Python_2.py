from typing import List

from toolkit import ListNode


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        stack = []
        for i in range(len(values) - 1, -1, -1):
            while stack and values[i] >= stack[-1]:
                stack.pop()
            stack.append(values[i])
            if len(stack) > 1:
                values[i] = stack[-2]
            else:
                values[i] = 0
        return values


if __name__ == "__main__":
    print(Solution().nextLargerNodes(ListNode([2, 1, 5])))  # [5,5,0]
    print(Solution().nextLargerNodes(ListNode([2, 7, 4, 3, 5])))  # [7,0,5,5,0]
    print(Solution().nextLargerNodes(ListNode([1, 7, 5, 1, 9, 2, 5, 1])))  # [7,9,9,9,0,5,0,0]
