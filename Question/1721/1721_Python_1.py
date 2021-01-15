from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1 = n2 = head
        for _ in range(k - 1):
            n2 = n2.next

        n3 = n2  # 正数第k个节点

        while n2.next:
            n1 = n1.next
            n2 = n2.next

        n4 = n1  # 倒数第k个节点

        n3.val, n4.val = n4.val, n3.val

        return head


if __name__ == "__main__":
    print(Solution().swapNodes(build_ListNode([1, 2, 3, 4, 5]), k=2))
    print(Solution().swapNodes(build_ListNode([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), k=5))
    print(Solution().swapNodes(build_ListNode([1]), k=1))
    print(Solution().swapNodes(build_ListNode([1, 2]), k=1))
    print(Solution().swapNodes(build_ListNode([1, 2, 3]), k=2))
