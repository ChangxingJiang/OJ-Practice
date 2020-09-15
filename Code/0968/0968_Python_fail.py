from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 计算树中所需监控最少数量
        # 返回值
        # 1. 父节点必须存在且必须有监控
        # 2. 父节点若存在则必须有监控
        # 3. 父节点若存在可以没有监控
        def dfs(node):
            # 处理空节点的情况
            if not node:
                return 0, 0, 0

            # 处理叶节点的情况
            if not node.left and not node.right:
                return 0, 1

            # 处理只有单侧子节点的情况
            if node.left and not node.right:
                a, b = dfs(node.left)
                return b, a + 1
            if node.right and not node.left:
                a, b = dfs(node.right)
                return b, a + 1

            # 处理拥有双侧子节点的情况
            a1, b1 = dfs(node.left)
            a2, b2 = dfs(node.right)
            return b1 + b2, a1 + a2 + 1

        return max(min(dfs(root)), 1)


if __name__ == "__main__":
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, 0])))  # 1
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, None, 0, None, None, 0])))  # 2
    print(Solution().minCameraCover(build_TreeNode([0])))  # 1
