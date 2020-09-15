from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def goodNodes(self, root: TreeNode, last_max=-10001) -> int:
        if not root:
            return 0
        elif root.val >= last_max:
            return self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val) + 1
        else:
            return self.goodNodes(root.left, last_max) + self.goodNodes(root.right, last_max)


if __name__ == "__main__":
    # 4
    print(Solution().goodNodes(build_TreeNode([3, 1, 4, 3, None, 1, 5])))

    # 3
    print(Solution().goodNodes(build_TreeNode([3, 3, None, 4, 2])))

    # 1
    print(Solution().goodNodes(build_TreeNode([1])))
