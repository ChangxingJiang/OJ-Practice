from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # 第一次遍历
        # O(N)
        ans = mark = node = ListNode(0)
        node.next = head
        while node:
            if node.val < 9:
                mark = node
            node = node.next

        # 第二次遍历
        # O(N)
        node = ans
        find = False
        while node:
            if node == mark:
                node.val += 1
                find = True
            elif find:
                node.val = 0
            node = node.next

        # 返回结果
        if ans.val == 0:
            return ans.next
        else:
            return ans


if __name__ == "__main__":
    # [1,2,4]
    print(Solution().plusOne(build_ListNode([1, 2, 3])))
