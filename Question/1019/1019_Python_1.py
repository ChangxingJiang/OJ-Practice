from typing import List

from toolkit import ListNode


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        ans = []
        idx = 0
        while head:
            ans.append(0)
            while stack and head.val > stack[-1][0]:
                ans[stack.pop()[1]] = head.val
            stack.append([head.val, idx])
            idx += 1
            head = head.next
        return ans


if __name__ == "__main__":
    print(Solution().nextLargerNodes(ListNode([2, 1, 5])))  # [5,5,0]
    print(Solution().nextLargerNodes(ListNode([2, 7, 4, 3, 5])))  # [7,0,5,5,0]
    print(Solution().nextLargerNodes(ListNode([1, 7, 5, 1, 9, 2, 5, 1])))  # [7,9,9,9,0,5,0,0]
