from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.hashmap = {}

    def max_depth(self, node):
        if not node:
            return 0
        if node in self.hashmap:
            return self.hashmap[node]
        else:
            depth = max(self.max_depth(node.left), self.max_depth(node.right)) + 1
            self.hashmap[node] = depth
            return depth

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth_left = self.max_depth(root.left)
        depth_right = self.max_depth(root.right)
        if depth_left == depth_right:
            return root
        elif depth_left > depth_right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)


if __name__ == "__main__":
    # [2,7,4]
    print(Solution().subtreeWithAllDeepest(build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])))
