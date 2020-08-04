from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        stack = [root]
        ans = []
        while stack:
            if now := stack[-1]:
                stack.append(now.left)
            else:
                stack.pop()
                if not stack:
                    break
                now = stack.pop()
                ans.append(now.val)
                stack.append(now.right)

        return ans


if __name__ == "__main__":
    print(Solution().inorderTraversal(build_TreeNode([1, None, 2, 3])))  # [1,3,2]
    print(Solution().inorderTraversal(build_TreeNode([1, 2])))  # [2,1]
    print(Solution().inorderTraversal(build_TreeNode([3, 1, None, None, 2])))  # [1,2,3]
