import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = collections.deque([root])
        reverse = False
        while queue:
            now_val = []
            for _ in range(len(queue)):
                node = queue.popleft()
                now_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reverse:
                ans.append(now_val[::-1])
            else:
                ans.append(now_val)

            reverse = not reverse

        return ans


if __name__ == "__main__":
    # [
    #   [3],
    #   [20,9],
    #   [15,7]
    # ]
    print(Solution().levelOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))
