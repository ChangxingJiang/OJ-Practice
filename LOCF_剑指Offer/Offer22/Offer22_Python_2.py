from toolkit import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        lst = []
        while head:
            lst.append(head)
            head = head.next
        return lst[-k]


if __name__ == "__main__":
    print(Solution().getKthFromEnd(ListNode([1, 2, 3, 4, 5]), k=2))  # 4->5
