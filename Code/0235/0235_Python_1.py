from toolkit import TreeNode, build_TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return 0, None
            find_num_left, find_left = helper(node.left)
            find_num_right, find_right = helper(node.right)
            find_num = 0
            if find_num_left == 2:
                return 2, find_left
            if find_num_right == 2:
                return 2, find_right
            if node.val == p.val or node.val == q.val:
                find_num += 1
            find_num += find_num_left + find_num_right
            if find_num == 2:
                return 2, node
            else:
                return find_num, None

        find_num, find_node = helper(root)
        if find_num == 2:
            return find_node


if __name__ == "__main__":
    tree = build_TreeNode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 6
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right))  # 2
