from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 计算完全二叉树的高度
        high = 0
        node = root
        while node:
            high += 1
            node = node.left

        # 处理特殊情况
        if high == 0:
            return 0
        if high == 1:
            return 1

        # 二分查找（每次找当前节点的最左侧叶节点是否存在）
        ans = 2 ** (high - 1) - 1
        now = 1
        now_node = root  # 当前二分的节点
        while now < high - 1:
            # 判断当前节点是否存在
            this_node = now_node.right  # 当前二分的右侧子节点
            this = now
            while this_node:
                this_node = this_node.left
                this += 1

            # 处理当前节点存在的情况
            if this == high:
                print(now, this, "->", 2 ** (this - now))
                now += 1
                ans += 2 ** (this - now)
                now_node = now_node.right

            # 处理当前节点不存在的情况
            else:
                print(now, this, "->", 0)
                now += 1
                now_node = now_node.left

        # 处理最后一次二分查找的情况
        if now_node.left:
            ans += 1
        if now_node.right:
            ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().countNodes(build_TreeNode([1, 2, 3, 4, 5, 6])))  # 6
