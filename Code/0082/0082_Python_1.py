from toolkit import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 处理特殊情况
        if not head:
            return None

        # 遍历删除重复值
        ans = node = ListNode(0)
        while head:
            if not head.next or head.val != head.next.val:
                node.next = ListNode(head.val)
                node = node.next
                head = head.next
            else:
                val = head.val
                while head and head.val == val:
                    head = head.next

        return ans.next


if __name__ == "__main__":
    print(Solution().deleteDuplicates(ListNode([1, 2, 3, 3, 4, 4, 5])))  # 1->2->5
    print(Solution().deleteDuplicates(ListNode([1, 1, 1, 2, 3])))  # 2->3
