from toolkit import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            ans = ListNode(0)
            ans.next = head
            node = head.next
            head.next = None
            while node:
                temp = ans.next
                ans.next = node
                node = node.next
                ans.next.next = temp
            return ans.next


if __name__ == "__main__":
    print(Solution().reverseList(ListNode([1, 2, 3, 4, 5])))  # [5,4,3,2,1]
