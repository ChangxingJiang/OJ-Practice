from toolkit import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            node = ListNode(head.val)
            node.next = ans
            ans = node
            head = head.next
        return ans


if __name__ == "__main__":
    print(Solution().reverseList(ListNode([1, 2, 3, 4, 5])))  # [5,4,3,2,1]
