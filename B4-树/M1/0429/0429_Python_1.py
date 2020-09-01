from typing import List

from toolkit import Node
from toolkit import build_Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [
    #      [1],
    #      [3,2,4],
    #      [5,6]
    # ]
    tree = build_Node([1, None, 3, 2, 4, None, 5, 6])
    print(Solution().levelOrder(tree))
