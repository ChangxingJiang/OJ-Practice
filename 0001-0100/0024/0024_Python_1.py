from toolkit import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = node = ListNode(0)
        ans.next = head
        while node.next and node.next.next:
            node1 = node.next
            node2 = node.next.next
            node1.next = node2.next
            node2.next = node1
            node.next = node2
            node = node.next.next
        return ans.next


if __name__ == "__main__":
    print(Solution().swapPairs(ListNode([1, 2, 3, 4])))  # 2->1->4->3
