from typing import List

from toolkit import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        values = []
        for node in lists:
            while node:
                heapq.heappush(values, node.val)
                node = node.next

        ans = node = ListNode(0)
        while values:
            node.next = ListNode(heapq.heappop(values))
            node = node.next

        return ans.next


if __name__ == "__main__":
    print("结果：")
    print(Solution().mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6])
    ]))  # 1->1->2->3->4->4->5->6
