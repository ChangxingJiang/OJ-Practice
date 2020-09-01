from typing import List

from toolkit import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        pass


if __name__ == "__main__":
    # [
    #   [1,null,3,2],
    #   [3,2,null,1],
    #   [3,1,null,null,2],
    #   [2,1,3],
    #   [1,null,2,null,3]
    # ]
    print(Solution().generateTrees(3))
