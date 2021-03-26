from toolkit import ListNode


class Solution:
    # 排序两个排序链表
    @staticmethod
    def helper(head1, head2):
        ans = node = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                node.next = ListNode(head1.val)
                node = node.next
                head1 = head1.next
            else:
                node.next = ListNode(head2.val)
                node = node.next
                head2 = head2.next

        if head1 or head2:
            node.next = head1 or head2

        return ans.next

    def sortList(self, head: ListNode) -> ListNode:
        # 处理特殊情况
        if not head or not head.next:
            return head

        # 获取链表中点
        slow = fast = head
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node2 = slow.next
        slow.next = None
        node1 = head

        return self.helper(self.sortList(node1), self.sortList(node2))


if __name__ == "__main__":
    print(Solution().sortList(ListNode([4, 2, 1, 3])))  # 1->2->3->4
    print(Solution().sortList(ListNode([-1, 5, 3, 4, 0])))  # -1->0->3->4->5
