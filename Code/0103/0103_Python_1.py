from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 处理特殊情况
        if not root:
            return []

        order_is_left = True
        ans = []
        now_line = [root]
        while now_line:
            ans_line = []
            next_line = []
            for node in now_line:
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
                ans_line.append(node.val)

            if order_is_left:
                ans.append(ans_line)
            else:
                ans.append(list(reversed(ans_line)))

            now_line = next_line
            order_is_left = not order_is_left

        return ans


if __name__ == "__main__":
    # [
    #   [3],
    #   [20,9],
    #   [15,7]
    # ]
    print(Solution().zigzagLevelOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))
