from LeetTool import ListNode
from LeetTool import build_ListNode

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    listNode = build_ListNode(["a", "b", "c", "d", "e", "f"])
    print(Solution().deleteNode(listNode.next.next))
    print(listNode)
