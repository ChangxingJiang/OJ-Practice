from toolkit import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        # 定位到链表中点（奇数个为绝对中点，偶数个为中线右侧）
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转链表中点后半段链表
        reverse = None
        while slow:
            temp = ListNode(slow.val)
            temp.next = reverse
            reverse = temp
            slow = slow.next
        # print(reverse, head)

        # 比较翻转后的后半段链表与前半段链表是否相同（如果为奇数则最后一次比较中点和中点自己是否相同）
        while reverse:
            if reverse.val != head.val:
                # print(reverse.val, head.val)
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
    print(Solution().isPalindrome(ListNode([1, 0, 1])))  # True
