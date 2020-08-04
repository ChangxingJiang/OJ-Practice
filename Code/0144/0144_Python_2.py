from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        stack = [root]
        ans = []
        while stack:
            now = stack[-1]
            if now:
                ans.append(now.val)
                stack.append(now.left)
            else:
                stack.pop()
                if not stack:
                    break
                now = stack.pop()
                stack.append(now.right)

        return ans


if __name__ == "__main__":
    print(Solution().preorderTraversal(build_TreeNode([1, None, 2, 3])))  # [1,2,3]
