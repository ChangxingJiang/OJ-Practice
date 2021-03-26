from toolkit import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node, curr = head, head
        for _ in range(n + 1):
            if not curr:
                return head.next
            curr = curr.next
        while curr:
            node = node.next
            curr = curr.next
        node.next = node.next.next
        return head


if __name__ == "__main__":
    print(Solution().removeNthFromEnd(ListNode([1, 2, 3, 4, 5]), n=2))  # 1->2->3->5
    print(Solution().removeNthFromEnd(ListNode([1]), n=1))  # None
