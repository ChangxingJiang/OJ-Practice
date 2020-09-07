from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 处理特殊情况
        if not root:
            return []

        ans = []
        now_node = [root]
        while now_node:
            now_val = []
            next_node = []
            for node in now_node:
                now_val.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            ans.append(now_val)
            now_node = next_node

        return ans


if __name__ == "__main__":
    # [
    #   [3],
    #   [9,20],
    #   [15,7]
    # ]
    print(Solution().levelOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))
