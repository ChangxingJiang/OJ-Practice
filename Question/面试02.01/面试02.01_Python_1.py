from toolkit import ListNode


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        lst = {head.val}
        node = head
        while node.next:
            if node.next.val not in lst:
                lst.add(node.next.val)
                node = node.next
            else:
                node.next = node.next.next
        return head


if __name__ == "__main__":
    print(Solution().removeDuplicateNodes(ListNode([1, 2, 3, 3, 2, 1])))  # [1,2,3]
    print(Solution().removeDuplicateNodes(ListNode([1, 1, 1, 1, 2])))  # [1,2]
