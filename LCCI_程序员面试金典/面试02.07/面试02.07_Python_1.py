from LeetTool import ListNode
from LeetTool import build_ListNode_with_skip


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        i1, i2 = headA, headB
        while i1 or i2:
            if i1 == i2:
                return i1

            i1 = i1.next
            i2 = i2.next

            # 处理未相交的情况
            if i1 is None and i2 is None:
                return None

            if i1 is None:
                i1 = headB
            if i2 is None:
                i2 = headA


if __name__ == "__main__":
    list1, list2 = build_ListNode_with_skip(8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3)
    print(Solution().getIntersectionNode(list1, list2))  # 8

    list1, list2 = build_ListNode_with_skip(2, [0, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    print(Solution().getIntersectionNode(list1, list2))  # 2

    list1, list2 = build_ListNode_with_skip(0, [2, 6, 4], [1, 5], 3, 2)
    print(Solution().getIntersectionNode(list1, list2))  # None

    list1, list2 = build_ListNode_with_skip(0, [1], [0], 1, 0)
    print(Solution().getIntersectionNode(list1, list2))  # None
