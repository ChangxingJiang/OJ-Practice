from toolkit import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
        if l1 or l2:
            node.next = l1 or l2
        return ans.next


if __name__ == "__main__":
    # 1->1->2->3->4->4
    print(Solution().mergeTwoLists(ListNode([1, 2, 4]), ListNode([1, 3, 4])))
