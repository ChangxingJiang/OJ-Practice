from toolkit import ListNode, build_ListNode_with_skip


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1


if __name__ == "__main__":
    list1, list2 = build_ListNode_with_skip(8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3)
    print(Solution().getIntersectionNode(list1, list2))  # 8

    list1, list2 = build_ListNode_with_skip(2, [0, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    print(Solution().getIntersectionNode(list1, list2))  # 2

    list1, list2 = build_ListNode_with_skip(0, [2, 6, 4], [1, 5], 3, 2)
    print(Solution().getIntersectionNode(list1, list2))  # None
