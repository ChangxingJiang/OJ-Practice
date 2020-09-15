from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


def inorder_traversal_to_iter(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.val
            node = node.right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 生成两棵二叉搜索树的中序遍历迭代器
        lst1 = inorder_traversal_to_iter(root1)
        lst2 = inorder_traversal_to_iter(root2)

        ans = []
        val1 = None
        val2 = None

        while True:
            if val1 is None:
                try:
                    val1 = next(lst1)
                except StopIteration:
                    try:
                        while True:
                            if val2 is not None:
                                ans.append(val2)
                            val2 = next(lst2)
                    except StopIteration:
                        break
            if val2 is None:
                try:
                    val2 = next(lst2)
                except StopIteration:
                    try:
                        while True:
                            ans.append(val1)
                            val1 = next(lst1)
                    except StopIteration:
                        break
            if val1 <= val2:
                ans.append(val1)
                val1 = None
            else:
                ans.append(val2)
                val2 = None

        return ans


if __name__ == "__main__":
    print(Solution().getAllElements(build_TreeNode([2, 1, 4]), build_TreeNode([1, 0, 3])))  # [0,1,1,2,3,4]
    print(Solution().getAllElements(build_TreeNode([0, -10, 10]), build_TreeNode([5, 1, 7, 0, 2])))  # [-10,0,0,1,2,5,7,10]
    print(Solution().getAllElements(build_TreeNode([]), build_TreeNode([5, 1, 7, 0, 2])))  # [0,1,2,5,7]
    print(Solution().getAllElements(build_TreeNode([0, -10, 10]), build_TreeNode([])))  # [-10,0,10]
    print(Solution().getAllElements(build_TreeNode([1, None, 8]), build_TreeNode([8, 1])))  # [1,1,8,8]
