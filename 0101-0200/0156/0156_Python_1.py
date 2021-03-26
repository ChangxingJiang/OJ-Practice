from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        ans = TreeNode(root.val)
        while root.left:
            node = TreeNode(root.left.val)
            node.right = ans
            node.left = root.right
            ans = node
            root = root.left
        return ans


if __name__ == "__main__":
    # [4,5,2,#,#,3,1]
    print(Solution().upsideDownBinaryTree(build_TreeNode([1, 2, 3, 4, 5])))
