from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        stack = [[root, False]]
        ans = []

        while stack:
            now = stack[-1]
            if now[0]:
                stack.append([now[0].left, False])
            else:
                stack.pop()
                if not stack:
                    break
                now = stack[-1]
                if not now[1]:  # 右子树尚未遍历
                    stack[-1][1] = True
                    stack.append([now[0].right, False])
                else:  # 左右子树均已遍历
                    ans.append(now[0].val)
                    stack.pop()
                    stack.append([None, True])

        return ans


if __name__ == "__main__":
    print(Solution().postorderTraversal(build_TreeNode([1, None, 2, 3])))  # [3,2,1]
