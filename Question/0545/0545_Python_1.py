from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # 寻找左边界
        left = []
        node = root
        if node.left:
            while node:
                left.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        else:
            # 根不存在左子树，故根自身即为左边界
            left = [root]

        # 寻找右边界
        right = []
        node = root
        if node.right:
            while node:
                right.append(node)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        else:
            # 根不存在右子树，故根自身即为右边界
            right = [root]
        right.reverse()

        # 寻找叶子节点
        leaf = []

        def dfs(node):
            if node:
                if node.left or node.right:
                    dfs(node.left)
                    dfs(node.right)
                else:
                    leaf.append(node)

        dfs(root)

        # print([p.val for p in left])
        # print([p.val for p in leaf])
        # print([p.val for p in right])

        # 处理只有一个节点的情况
        if left == leaf == right:
            return [p.val for p in left]

        # 合成结果
        ans = []

        if left[-1] == leaf[0]:
            ans += [p.val for p in left[:-1]]
        else:
            ans += [p.val for p in left]

        if leaf[-1] == right[0]:
            ans += [p.val for p in leaf[:-1]]
        else:
            ans += [p.val for p in leaf]

        if right[-1] == left[0]:
            ans += [p.val for p in right[:-1]]
        else:
            ans += [p.val for p in right]

        return ans


if __name__ == "__main__":
    # [1]
    print(Solution().boundaryOfBinaryTree(build_TreeNode([1])))

    # [1,3,4,2]
    print(Solution().boundaryOfBinaryTree(build_TreeNode([1, None, 2, 3, 4])))

    # [1,2,4,7,8,9,10,6,3]
    print(Solution().boundaryOfBinaryTree(build_TreeNode([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])))
