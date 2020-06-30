from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        now_level = [root]
        while len(now_level) > 0:
            nums = []
            next_level = []
            for node in now_level:
                if node:
                    nums.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            ans.append(sum(nums) / len(nums))
            now_level = next_level
        return ans


if __name__ == "__main__":
    print(Solution().averageOfLevels(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # [3,14.5,11]
