from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, None
        node = list1
        while node:
            if node.next and node.next.val == a:
                start = node
            if node.val == b:
                end = node.next
            node = node.next

        node = list2
        while node.next:
            node = node.next
        node.next = end
        start.next = list2

        return list1


if __name__ == "__main__":
    # [0,1,2,1000000,1000001,1000002,5]
    print(Solution().mergeInBetween(build_ListNode([0, 1, 2, 3, 4, 5]), 3, 4,
                                    build_ListNode([1000000, 1000001, 1000002])))

    # [0,1,1000000,1000001,1000002,1000003,1000004,6]
    print(Solution().mergeInBetween(build_ListNode([0, 1, 2, 3, 4, 5, 6]), 3, 4,
                                    build_ListNode([1000000, 1000001, 1000002, 1000003, 1000004])))
