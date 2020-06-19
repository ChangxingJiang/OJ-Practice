from toolkit import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = node = ListNode(0)
        ans.next = node.next = head
        while node and node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next
        return ans.next


if __name__ == "__main__":
    print(Solution().removeElements(ListNode([1, 2, 6, 3, 4, 5, 6]), 6))
