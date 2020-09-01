from toolkit import TreeNode
from toolkit import build_TreeNode
from typing import List
from typing import Dict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pass
if __name__ == "__main__":
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    print(Solution().pathSum(build_TreeNode([5,4,8,11,None,13,4,7,2,None,None,5,1]),22))
