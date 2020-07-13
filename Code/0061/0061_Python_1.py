from toolkit import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        k = k % size

        start = head

        ans = node = ListNode(0)

        for _ in range(size - k):
            node.next = ListNode(start.val)
            node = node.next
            start = start.next

        node = ans
        while start:
            now = ListNode(start.val)
            now.next = node.next
            node.next = now
            node = node.next
            start = start.next

        return ans.next


if __name__ == "__main__":
    print(Solution().rotateRight(ListNode([1, 2, 3, 4, 5]), k=2))  # 4->5->1->2->3
    print(Solution().rotateRight(ListNode([0, 1, 2]), k=4))  # 2->0->1
