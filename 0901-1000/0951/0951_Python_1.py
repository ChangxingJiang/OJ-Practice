from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 处理两个节点均不存在的情况
        if not root1 and not root2:
            return True

        # 处理两个节点有一个存在的情况
        if not root1 or not root2:
            return False

        # 处理两个根节点不相等的情况
        if root1.val != root2.val:
            return False

        # 处理两个根节点相等的情况
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


if __name__ == "__main__":
    print(Solution().flipEquiv(
        root1=build_TreeNode([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
        root2=build_TreeNode([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])))  # True
