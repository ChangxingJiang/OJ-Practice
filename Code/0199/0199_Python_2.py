from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        # 处理一般情况
        ans = [root.val]
        now_node = [root]
        while now_node:
            node_most_right = None
            next_node = []
            for node in now_node:
                if node.right:
                    next_node.append(node.right)
                    if not node_most_right:
                        node_most_right = node.right
                if node.left:
                    next_node.append(node.left)
                    if not node_most_right:
                        node_most_right = node.left
            if next_node:
                ans.append(node_most_right.val)
            now_node = next_node

        return ans


if __name__ == "__main__":
    print(Solution().rightSideView(build_TreeNode([1, 2, 3, None, 5, None, 4])))  # [1,3,4]
    print(Solution().rightSideView(build_TreeNode([1, 2])))  # [1,2]
