from toolkit import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = node = ListNode(0)
        while head:
            if head.val != val:
                node.next = ListNode(head.val)
                node = node.next
            head = head.next
        return ans.next


if __name__ == "__main__":
    print(Solution().removeElements(ListNode([1, 2, 6, 3, 4, 5, 6]), 6))
