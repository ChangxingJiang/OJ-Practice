from typing import List

from toolkit import ListNode


class Solution:
    # 合并两个顺序链表
    @staticmethod
    def helper(listNode1, listNode2):
        ans = node = ListNode(0)
        while listNode1 and listNode2:
            if listNode1.val < listNode2.val:
                node.next = ListNode(listNode1.val)
                listNode1 = listNode1.next
                node = node.next
            else:
                node.next = ListNode(listNode2.val)
                listNode2 = listNode2.next
                node = node.next
        if listNode1 or listNode2:
            node.next = listNode1 or listNode2
        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        return Solution.helper(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))


if __name__ == "__main__":
    print("结果：")
    print(Solution().mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6])
    ]))  # 1->1->2->3->4->4->5->6
