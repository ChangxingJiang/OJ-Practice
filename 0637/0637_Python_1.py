from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        pass


if __name__ == "__main__":
    print(Solution().averageOfLevels(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # [3,14.5,11]
