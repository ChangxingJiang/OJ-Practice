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
        stack = [(root, 0)]
        while stack:
            node, level = stack[-1]
            if node.right:
                stack.append((node.right, level + 1))
                if level + 1 == len(ans):
                    ans.append(node.right.val)
            else:
                while stack:
                    node, level = stack.pop()
                    if node.left:
                        stack.append((node.left, level + 1))
                        if level + 1 == len(ans):
                            ans.append(node.left.val)
                        break
        return ans


if __name__ == "__main__":
    print(Solution().rightSideView(build_TreeNode([1, 2, 3, None, 5, None, 4])))  # [1,3,4]
    print(Solution().rightSideView(build_TreeNode([1, 2])))  # [1,2]
