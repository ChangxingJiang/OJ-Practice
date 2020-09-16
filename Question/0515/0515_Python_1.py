import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        ans = []
        queue = collections.deque([root])

        while queue:
            max_val = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)

        return ans


if __name__ == "__main__":
    # [1,3,9]
    print(Solution().largestValues(build_TreeNode([1, 3, 2, 5, 3, None, 9])))
