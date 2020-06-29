from typing import List

from toolkit import Node, build_Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().preorder(build_Node([1, None, 3, 2, 4, None, 5, 6])))  # [1,3,5,6,2,4]
