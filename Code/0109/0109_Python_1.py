from toolkit import ListNode
from toolkit import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        # 边界处理
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # 二分处理
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tree = TreeNode(slow.next.val)
        tree.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        tree.left = self.sortedListToBST(head)
        return tree


if __name__ == "__main__":
    # [0,-3,9,-10,None,5]
    print(Solution().sortedListToBST(ListNode([-10, -3, 0, 5, 9])))
