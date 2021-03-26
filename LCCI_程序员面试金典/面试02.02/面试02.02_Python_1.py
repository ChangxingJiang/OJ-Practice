from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        i1, i2 = head, head

        for _ in range(k - 1):
            i1 = i1.next

        while i1.next:
            i1 = i1.next
            i2 = i2.next

        return i2.val


if __name__ == "__main__":
    print(Solution().kthToLast(build_ListNode([1, 2, 3, 4, 5]), 2))  # 4
