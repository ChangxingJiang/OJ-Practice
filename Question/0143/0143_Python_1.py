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

        # 翻转链表后半部分
        curr = slow.next
        while curr and curr.next:
            now = ListNode(curr.next.val)
            now.next = slow.next
            slow.next = now
            curr.next = curr.next.next

        # 重排链表
        node = head
        while node != slow and slow.next:
            now = ListNode(slow.next.val)
            now.next = node.next
            node.next = now
            node = node.next.next
            slow.next = slow.next.next


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4])
    Solution().reorderList(head)
    print(head)  # 1->4->2->3

    head = ListNode([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(head)  # 1->5->2->4->3
