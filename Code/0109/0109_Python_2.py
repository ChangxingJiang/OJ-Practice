from toolkit import ListNode
from toolkit import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 异常情况处理
        if not head:
            return None

        # 二分处理
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)

        # 定义递归函数
        def helper(vals):
            # 边界处理
            if len(vals) == 0:
                return None
            if len(vals) == 1:
                return TreeNode(vals[0])

            # 二分处理
            mid = len(vals) // 2
            tree = TreeNode(vals[mid])
            tree.left = helper(vals[:mid])
            tree.right = helper(vals[mid + 1:])
            return tree

        # 递归得到结果
        return helper(values)


if __name__ == "__main__":
    # [0,-3,9,-10,None,5]
    print(Solution().sortedListToBST(ListNode([-10, -3, 0, 5, 9])))
