from toolkit import TreeNode, build_TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def helper(node1, node2):
            if node1 and node2:
                node = TreeNode(node1.val + node2.val)
                node.left = helper(node1.left, node2.left)
                node.right = helper(node1.right, node2.right)
                return node
            elif node1:
                return node1
            elif node2:
                return node2
            else:
                return None

        return helper(t1, t2)


if __name__ == "__main__":
    # [3,4,5,5,4,None,7]
    print(Solution().mergeTrees(build_TreeNode([1, 3, 2, 5]),
                                build_TreeNode([2, 1, 3, None, 4, None, 7])))
