from typing import List
from typing import Dict

from LeetTool import TreeNode
from LeetTool import build_TreeNode
from LeetTool import ListNode
from LeetTool import build_ListNode
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        pass
if __name__ == "__main__":
    print(Solution().ways(pizza = ["A..","AAA","..."], k = 3))  # 3
    print(Solution().ways(pizza = ["A..","AA.","..."], k = 3))  # 1
    print(Solution().ways(pizza = ["A..","A..","..."], k = 1))  # 1