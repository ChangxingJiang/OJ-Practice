from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 贪心算法：每个节点在选择装监控的方案时，都尽可能让装的监控更靠近根节点
        # 返回值：1. 当前节点下安装监控的最小数量
        #        2. 当前节点的父节点是否必须安装监控：1=距离最近监控为1个单位距离；2=距离当前最近监控为2个单位距离；3=距离当前最近监控为3个单位距离
        def dfs(node):
            # 处理节点不存在的情况
            if not node:
                return 0, 2

            # 处理节点为叶节点的情况
            if not node.left and not node.right:
                # 处理当前节点为根节点的情况
                if node == root:
                    return 1, 1

                # 处理当前节点不是根节点的情况（与子节点没有安装监控的情况相当）
                else:
                    return 0, 3

            # 处理当前节点不是叶节点的情况
            n_left, d_left = dfs(node.left)
            n_right, d_right = dfs(node.right)
            dd = sorted([d_left, d_right])
            if dd[0] == 1 and dd[1] in {1, 2}:  # 左节点或右节点有一个已经安装监控，且另外一个子结点的至少一个子节点也已经安装监控
                return n_left + n_right, 2
            elif dd[1] == 3:
                return n_left + n_right + 1, 1  # 左节点或右节点中至少有一个的所有子节点都没有安装监控
            else:  # dd = [2,2]  左节点和右节点都没有安装监控，但是它们都至少有一个子节点安装了监控
                if node == root:
                    return n_left + n_right + 1, 1

                # 处理当前节点不是根节点的情况
                else:
                    return n_left + n_right, 3

        return dfs(root)[0]


if __name__ == "__main__":
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, 0])))  # 1
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, None, 0, None, None, 0])))  # 2
    print(Solution().minCameraCover(build_TreeNode([0])))  # 1
    print(Solution().minCameraCover(build_TreeNode([0, None, 0, None, 0, None, 0])))  # 2
    print(Solution().minCameraCover(build_TreeNode([0, 0, 0, None, 0, 0, None, None, 0])))  # 2
