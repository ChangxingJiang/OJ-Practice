from typing import List

from toolkit import Node
from toolkit import build_Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 处理特殊情况
        if not root:
            return []

        # 处理一般情况
        ans = []
        now_node = [root]
        while now_node:
            now_val = []
            next_node = []
            for node in now_node:
                now_val.append(node.val)
                if node.children:
                    for child in node.children:
                        next_node.append(child)
            ans.append(now_val)
            now_node = next_node

        return ans


if __name__ == "__main__":
    # [
    #      [1],
    #      [3,2,4],
    #      [5,6]
    # ]
    tree = build_Node([1, None, 3, 2, 4, None, 5, 6])
    print(Solution().levelOrder(tree))
