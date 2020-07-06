from toolkit import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().rotateRight(ListNode([1, 2, 3, 4, 5]), k=2))  # 4->5->1->2->3
    print(Solution().rotateRight(ListNode([0, 1, 2]), k=4))  # 2->0->1
