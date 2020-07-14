from typing import List

from toolkit import ListNode


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        ans = 0
        part = False
        while head:
            if head.val in G:
                if not part:
                    ans += 1
                    part = True
            else:
                part = False
            head = head.next
        return ans


if __name__ == "__main__":
    print(Solution().numComponents(ListNode([0, 1, 2, 3]), [0, 1, 3]))  # 2
    print(Solution().numComponents(ListNode([0, 1, 2, 3, 4]), [0, 3, 1, 4]))  # 2
