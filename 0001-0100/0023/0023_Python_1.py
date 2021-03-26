from typing import List

from toolkit import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = node = ListNode(0)
        while any(lists):
            min_node = ListNode(float("inf"))
            min_num = -1
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_node.val:
                    min_num = i
                    min_node = ListNode(lists[i].val)
            lists[min_num] = lists[min_num].next
            node.next = min_node
            node = node.next
        return ans.next


if __name__ == "__main__":
    print(Solution().mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6])
    ]))  # 1->1->2->3->4->4->5->6
