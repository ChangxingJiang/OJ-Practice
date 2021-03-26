from toolkit import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    node_list = ListNode([4, 5, 1, 9])
    print(Solution().deleteNode(node_list.next), node_list)
    node_list = ListNode([4, 5, 1, 9])
    print(Solution().deleteNode(node_list.next.next), node_list)
