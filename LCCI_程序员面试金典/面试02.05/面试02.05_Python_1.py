from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(0)
        last = 0  # 进位数量
        while l1 or l2 or last:
            now = last

            if l1:
                now += l1.val
                l1 = l1.next
            if l2:
                now += l2.val
                l2 = l2.next

            last, now = divmod(now, 10)

            node.next = ListNode(now)
            node = node.next

        return head.next


if __name__ == "__main__":
    print(Solution().addTwoNumbers(build_ListNode([7, 1, 6]), build_ListNode([5, 9, 2])))  # 2->1->9
    print(Solution().addTwoNumbers(build_ListNode([6, 1, 7]), build_ListNode([2, 9, 5])))  # 9->1->2
