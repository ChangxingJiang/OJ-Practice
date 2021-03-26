from toolkit import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == "__main__":
    print(Solution().getKthFromEnd(ListNode([1, 2, 3, 4, 5]), k=2))  # 4->5
