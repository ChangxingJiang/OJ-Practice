from typing import List

from toolkit import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst[::-1]


if __name__ == "__main__":
    print(Solution().reversePrint(ListNode([1, 3, 2])))  # [2,3,1]
