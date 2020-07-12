from toolkit import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 寻找链表中点（快慢针法）
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转后半部分链表
        reverse = None
        while slow:
            node = ListNode(slow.val)
            node.next = reverse
            reverse = node
            slow = slow.next

        # 比较链表是否相同
        while reverse:
            if reverse.val != head.val:
                return False
            head = head.next
            reverse = reverse.next
        else:
            return True


if __name__ == "__main__":
    print(Solution().isPalindrome(ListNode([1, 2])))  # False
    print(Solution().isPalindrome(ListNode([1, 2, 2, 1])))  # True
    print(Solution().isPalindrome(ListNode([1])))  # True
    print(Solution().isPalindrome(ListNode([1, 2, 1])))  # True
    print(Solution().isPalindrome(None))  # True
