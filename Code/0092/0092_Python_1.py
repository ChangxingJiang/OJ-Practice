from toolkit import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 处理特殊情况
        if not head:
            return None

        # 找到翻转部分的前一个元素
        ans = node = ListNode(0)
        ans.next = head
        for _ in range(m - 1):
            node = node.next

        # 翻转链表
        curr = node.next
        for _ in range(n - m):
            now = ListNode(curr.next.val)
            now.next = node.next
            node.next = now
            curr.next = curr.next.next

        return ans.next


if __name__ == "__main__":
    print(Solution().reverseBetween(ListNode([1, 2, 3, 4, 5]), m=2, n=4))  # 1->4->3->2->5
