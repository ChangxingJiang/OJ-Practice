import collections
from typing import List

from toolkit import ListNode
from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        tree_nodes = collections.deque([tree])
        while tree_nodes:
            head = node = ListNode(0)
            for i in range(len(tree_nodes)):
                now = tree_nodes.popleft()
                if now.left:
                    tree_nodes.append(now.left)
                if now.right:
                    tree_nodes.append(now.right)
                node.next = ListNode(now.val)
                node = node.next
            ans.append(head.next)

        return ans


if __name__ == "__main__":
    # [[1],[2,3],[4,5,7],[8]]
    print(Solution().listOfDepth(build_TreeNode([1, 2, 3, 4, 5, None, 7, 8])))
