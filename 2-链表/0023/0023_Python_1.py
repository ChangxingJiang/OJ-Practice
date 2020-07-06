from typing import List

from toolkit import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6])
    ]))  # 1->1->2->3->4->4->5->6
