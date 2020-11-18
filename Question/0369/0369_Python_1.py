from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        lst = []

        ans = node = ListNode(0)
        node.next = head
        while node:
            lst.append(node)
            node = node.next

        while lst:
            if lst[-1].val < 9:
                lst[-1].val += 1
                break
            else:
                lst[-1].val = 0
                lst.pop()

        if ans.val == 0:
            return ans.next
        else:
            return ans


if __name__ == "__main__":
    # [1,2,4]
    print(Solution().plusOne(build_ListNode([1, 2, 3])))
