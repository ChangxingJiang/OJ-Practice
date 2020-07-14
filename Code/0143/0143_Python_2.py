from toolkit import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 处理特殊情况
        if not head or not head.next:
            return

        # 寻找链表中点
        slow = fast = head
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 移除后半部分链表
        curr = slow.next
        slow.next = None

        # 翻转链表后半部分
        reverse = None
        while curr:
            point = curr.next
            curr.next = reverse
            reverse = curr
            curr = point

        # 重排链表
        while head and head.next:
            point = reverse.next
            reverse.next = head.next
            head.next = reverse
            head = head.next.next
            reverse = point
        if reverse:
            head.next = reverse


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4])
    Solution().reorderList(head)
    print(head)  # 1->4->2->3

    head = ListNode([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(head)  # 1->5->2->4->3
