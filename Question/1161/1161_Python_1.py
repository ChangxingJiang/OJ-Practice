import collections

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = collections.deque([root])
        ans_idx, ans_val = 1, root.val
        level_idx = 1
        while level:
            level_val = 0
            for i in range(len(level)):
                p = level.popleft()
                level_val += p.val
                if p.left:
                    level.append(p.left)
                if p.right:
                    level.append(p.right)
            if ans_val < level_val:
                ans_idx, ans_val = level_idx, level_val
            level_idx += 1
        return ans_idx


if __name__ == "__main__":
    # 2
    print(Solution().maxLevelSum(build_TreeNode([1, 7, 0, 7, -8, None, None])))

    # 2
    print(Solution().maxLevelSum(build_TreeNode([989, None, 10250, 98693, -89388, None, None, None, -32127])))
