from typing import List

from toolkit import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = []
        for linked in lists:
            while linked:
                values.append(linked.val)
                linked = linked.next
        values.sort()

        ans = node = ListNode(0)
        for v in values:
            node.next = ListNode(v)
            node = node.next

        return ans.next


if __name__ == "__main__":
    print("结果：")
    print(Solution().mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6])
    ]))  # 1->1->2->3->4->4->5->6
