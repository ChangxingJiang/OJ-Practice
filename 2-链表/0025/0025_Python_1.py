from toolkit import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().reverseKGroup(ListNode([1, 2, 3, 4, 5]), k=2))  # 2->1->4->3->5
    print(Solution().reverseKGroup(ListNode([1, 2, 3, 4, 5]), k=3))  # 3->2->1->4->5
