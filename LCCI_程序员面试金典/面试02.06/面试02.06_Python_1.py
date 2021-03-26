from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        i1 = i2 = head

        # 快慢针求中点
        while i1 and i1.next:
            i1 = i1.next.next
            i2 = i2.next

        # 翻转链表
        i3 = None
        while i2:
            last = i2.next
            i2.next = i3
            i3 = i2
            i2 = last

        # 比较链表
        i4 = head
        while i3 and i4:
            if i3.val != i4.val:
                return False
            i3 = i3.next
            i4 = i4.next

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(build_ListNode([1, 2])))  # False
    print(Solution().isPalindrome(build_ListNode([1, 2, 2, 1])))  # True
