from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        pass


if __name__ == "__main__":
    # [["", "1", ""],
    #  ["2", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2])))

    # [["", "", "", "1", "", "", ""],
    #  ["", "2", "", "", "", "3", ""],
    #  ["", "", "4", "", "", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2, 3, None, 4])))

    # [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
    #  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
    #  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
    #  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2, 5, 3, None, 4])))
