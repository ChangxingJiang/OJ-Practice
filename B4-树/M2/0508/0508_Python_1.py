from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().findFrequentTreeSum(build_TreeNode([5, 2, -3])))  # [2,-3,4]
    print(Solution().findFrequentTreeSum(build_TreeNode([5, 2, -5])))  # [2]
