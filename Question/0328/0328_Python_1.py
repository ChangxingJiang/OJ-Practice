from toolkit import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd_node = ListNode(0)
        even_head = even_node = ListNode(0)
        is_odd = True
        while head:
            point = head.next
            head.next = None
            if is_odd:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            is_odd = not is_odd
            head = point
        odd_node.next = even_head.next
        return odd_head.next


if __name__ == "__main__":
    print(Solution().oddEvenList(ListNode([1, 2, 3, 4, 5])))  # 1->3->5->2->4
    print(Solution().oddEvenList(ListNode([2, 1, 3, 5, 6, 4, 7])))  # 2->3->6->7->1->5->4
