from toolkit import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ans = node = ListNode(0)
        ans.next = head
        while node:
            # 判断链表剩余长度是否充足
            curr = node
            is_enough = True
            for _ in range(k):
                if curr is None or curr.next is None:
                    is_enough = False
                    break
                curr = curr.next
            if not is_enough:
                break

            # 翻转链表
            curr = node.next
            for _ in range(k - 1):
                now = ListNode(curr.next.val)
                now.next = node.next
                node.next = now
                curr.next = curr.next.next

            node = curr

        return ans.next


if __name__ == "__main__":
    print(Solution().reverseKGroup(ListNode([1, 2, 3, 4, 5]), k=2))  # 2->1->4->3->5
    print(Solution().reverseKGroup(ListNode([1, 2, 3, 4, 5]), k=3))  # 3->2->1->4->5
    print(Solution().reverseKGroup(ListNode([1, 2]), k=2))  # 2->1
