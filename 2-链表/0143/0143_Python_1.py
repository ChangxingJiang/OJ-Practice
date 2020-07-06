from toolkit import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4])
    Solution().reorderList(head)
    print(head)  # 1->4->2->3

    head = ListNode([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(head)  # 1->5->2->4->3
