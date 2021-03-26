from typing import List

from toolkit import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def recursor(start, end):
            # 处理没有根节点的情况
            if start > end:
                return [None]

            # 处理只剩一个根节点的情况
            elif start == end:
                return [TreeNode(start)]

            # 处理还有多种根节点的情况
            ans = []
            for i in range(start, end + 1):
                left_trees = recursor(start, i - 1)
                right_trees = recursor(i + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        ans.append(node)

            return ans

        return recursor(1, n) if n else []


if __name__ == "__main__":
    # [
    #   [1,null,3,2],
    #   [3,2,null,1],
    #   [3,1,null,null,2],
    #   [2,1,3],
    #   [1,null,2,null,3]
    # ]
    print(Solution().generateTrees(3))

    # []
    print(Solution().generateTrees(0))
