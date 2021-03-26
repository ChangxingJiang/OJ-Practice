from toolkit import TreeNode, build_TreeNode


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        def helper(node, sums):
            # 处理树末端的情况
            if node is None:
                return 0

            # 统计当前路径和列表
            sums = [t + node.val for t in sums] + [node.val]

            # 继续检查子节点
            return sums.count(s) + helper(node.left, sums) + helper(node.right, sums)

        return helper(root, [])


if __name__ == "__main__":
    tree = build_TreeNode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(Solution().pathSum(tree, 8))  # 3
