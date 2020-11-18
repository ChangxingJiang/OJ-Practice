from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def convertBiNode(self, root: TreeNode, bigger=None) -> TreeNode:
        if root:
            # 处理当前节点
            left, right = root.left, root.right
            root.left = None

            # 处理当前节点的右侧节点
            if right:
                root.right = self.convertBiNode(right, bigger)
            else:
                root.right = bigger

            if left:
                return self.convertBiNode(left, root)
            else:
                return root


if __name__ == "__main__":
    # []
    print(Solution().convertBiNode(None))

    # [0,None,1,None,2,None,3,None,4,None,5,None,6]
    print(Solution().convertBiNode(build_TreeNode([4, 2, 5, 1, 3, None, 6, 0])))
