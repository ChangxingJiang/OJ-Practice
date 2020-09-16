import collections

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = 0
        queue = collections.deque([root])
        while queue:
            ans = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


if __name__ == "__main__":
    # 15
    print(Solution().deepestLeavesSum(build_TreeNode([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])))
