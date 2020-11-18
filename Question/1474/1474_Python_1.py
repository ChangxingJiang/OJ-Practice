from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = ListNode(0)
        node.next = head
        mm, nn = m, n
        while node:
            if mm:
                node = node.next
                mm -= 1
            elif nn:
                if node.next:
                    node.next = node.next.next
                else:
                    node.next = None
                nn -= 1
            else:
                mm, nn = m, n
        return head


if __name__ == "__main__":
    # [1,2,6,7,11,12]
    print(Solution().deleteNodes(build_ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 2, 3))

    # [1,5,9]
    print(Solution().deleteNodes(build_ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1, 3))

    # [1,2,3,5,6,7,9,10,11]
    print(Solution().deleteNodes(build_ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 3, 1))

    # [9,7,8]
    print(Solution().deleteNodes(build_ListNode([9, 3, 7, 7, 9, 10, 8, 2]), 1, 2))
