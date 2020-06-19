from toolkit import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head:
            temp = ListNode(head.val)
            temp.next = node
            node = temp
            head = head.next
        return node


if __name__ == "__main__":
    print(Solution().reverseList(ListNode([1, 2, 3, 4, 5])))  # [5,4,3,2,1]
