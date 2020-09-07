from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        while stack:
            if node := stack[-1]:
                stack.append(node.left)
            else:
                stack.pop()
                if not stack:
                    break
                node = stack.pop()
                stack.append(node.right)

                # 检查是否已经找到第k小的结果
                if k > 1:
                    k -= 1
                else:
                    return node.val


if __name__ == "__main__":
    print(Solution().kthSmallest(build_TreeNode([3, 1, 4, None, 2]), 1))  # 1
    print(Solution().kthSmallest(build_TreeNode([5, 3, 6, 2, 4, None, None, 1]), 3))  # 3
