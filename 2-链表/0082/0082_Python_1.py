from toolkit import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().deleteDuplicates(ListNode([1, 2, 3, 3, 4, 4, 5])))  # 1->2->5
    print(Solution().deleteDuplicates(ListNode([1, 1, 1, 2, 3])))  # 2->3
