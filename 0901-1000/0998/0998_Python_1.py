from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        # 处理目标值大于根节点的情况
        if val > root.val:
            new = TreeNode(val)
            new.left = root
            return new

        # 处理目标值小于根节点的情况
        last = root
        node = root.right
        while node and val < node.val:
            last = node
            node = node.right
        new = TreeNode(val)
        new.left = node
        last.right = new
        return root


if __name__ == "__main__":
    # [5,4,null,1,3,null,null,2]
    print(Solution().insertIntoMaxTree(build_TreeNode([4, 1, 3, None, None, 2]), 5))

    # [5,2,4,null,1,null,3]
    print(Solution().insertIntoMaxTree(build_TreeNode([5, 2, 4, None, 1]), 3))

    # [5,2,4,null,1,3]
    print(Solution().insertIntoMaxTree(build_TreeNode([5, 2, 3, None, 1]), 4))
