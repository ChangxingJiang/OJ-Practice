import copy

from toolkit import TreeNode, build_TreeNode


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        self.ans = 0

        def helper(node, source):
            # 处理树末端的情况
            if node is None:
                return

            # 计算当前路径
            source.append(node.val)

            # 判断路径是否等于目标值
            for i in range(len(source)):
                if sum(source[i:]) == s:
                    self.ans += 1

            # 继续检查子节点
            if node.left is not None:
                helper(node.left, copy.deepcopy(source))
            if node.right is not None:
                helper(node.right, copy.deepcopy(source))

        helper(root, [])

        return self.ans


if __name__ == "__main__":
    tree = build_TreeNode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(Solution().pathSum(tree, 8))  # 3
