import collections

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        ans = root.val
        queue = collections.deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                ans = queue[0].val

        return ans


if __name__ == "__main__":
    # 1
    print(Solution().findBottomLeftValue(build_TreeNode([2, 1, 3])))

    # 7
    print(Solution().findBottomLeftValue(build_TreeNode([1, 2, 3, 4, None, 5, 6, None, None, 7])))
