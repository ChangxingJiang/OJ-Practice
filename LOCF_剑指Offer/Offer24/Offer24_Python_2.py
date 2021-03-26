from toolkit import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            ans = ListNode(0)
            ans.next, node, head.next = head, head.next, None
            while node:
                ans.next, node.next, node = node, ans.next, node.next
            return ans.next


if __name__ == "__main__":
    print(Solution().reverseList(ListNode([1, 2, 3, 4, 5])))  # [5,4,3,2,1]
