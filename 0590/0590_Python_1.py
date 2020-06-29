from typing import List

from toolkit import Node, build_Node


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().postorder(build_Node([1, None, 3, 2, 4, None, 5, 6])))  # [5,6,3,2,4,1]
