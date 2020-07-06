from toolkit import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().oddEvenList(ListNode([1, 2, 3, 4, 5])))  # 1->3->5->2->4
    print(Solution().oddEvenList(ListNode([2, 1, 3, 5, 6, 4, 7])))  # 2->3->6->7->1->5->4
