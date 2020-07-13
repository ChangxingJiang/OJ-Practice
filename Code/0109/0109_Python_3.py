from toolkit import ListNode
from toolkit import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 异常情况处理
        if not head:
            return None

        # 计算链表长度
        size = 1
        node = head
        while node.next:
            node = node.next
            size += 1
        print(size)

        # 定义递归函数
        def helper(start, end):
            nonlocal head

            # 边界处理
            if start > end:
                return None

            # 递归处理
            mid = (end + start) // 2
            left = helper(start, mid - 1)  # 处理左半部分
            tree = TreeNode(head.val)  # 取出当前树的值（链表刚好遍历的这个位置）
            tree.left = left
            head = head.next
            tree.right = helper(mid + 1, end)  # 处理右半部分
            return tree

        # 递归得到结果
        return helper(0, size - 1)


if __name__ == "__main__":
    # [0,-3,9,-10,None,5]
    print(Solution().sortedListToBST(ListNode([-10, -3, 0, 5, 9])))
