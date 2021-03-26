from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode, now_val=0) -> int:
        # 处理当前节点不存在的情况
        if not root:
            return 0

        new_val = now_val * 10 + root.val

        # 处理当前节点非叶节点的情况
        if root.left or root.right:
            return self.sumNumbers(root.left, new_val) + self.sumNumbers(root.right, new_val)

        # 处理当前节点为叶节点的情况
        else:
            return new_val


if __name__ == "__main__":
    print(Solution().sumNumbers(build_TreeNode([1, 2, 3])))  # 25
    print(Solution().sumNumbers(build_TreeNode([4, 9, 0, 5, 1])))  # 1026
