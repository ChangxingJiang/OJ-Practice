from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = node1 = ListNode(0)
        head2 = node2 = ListNode(0)

        while head:
            if head.val >= x:
                node2.next = ListNode(head.val)
                node2 = node2.next
            else:
                node1.next = ListNode(head.val)
                node1 = node1.next
            head = head.next

        node1.next = head2.next

        return head1.next


if __name__ == "__main__":
    # 3->1->2->10->5->5->8
    print(Solution().partition(build_ListNode([3, 5, 8, 5, 10, 2, 1]), 5))
