from toolkit import ListNode


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    node_list = ListNode([4, 5, 1, 9])
    print(Solution().deleteNode(node_list.next))
    print(Solution().deleteNode(node_list.next.next))
