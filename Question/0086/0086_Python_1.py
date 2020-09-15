from toolkit import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        headA = nodeA = ListNode(0)
        headB = nodeB = ListNode(0)
        while head:
            if head.val < x:
                nodeA.next = ListNode(head.val)
                nodeA = nodeA.next
            else:
                nodeB.next = ListNode(head.val)
                nodeB = nodeB.next
            head = head.next
        nodeA.next = headB.next
        return headA.next


if __name__ == "__main__":
    print(Solution().partition(ListNode([1, 4, 3, 2, 5, 2]), x=3))  # 1->2->2->4->3->5
