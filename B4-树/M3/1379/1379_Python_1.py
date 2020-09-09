import copy

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    # 3
    tree1 = build_TreeNode([7, 4, 3, None, None, 6, 19])
    tree2 = copy.deepcopy(tree1)
    print(Solution().getTargetCopy(tree1, tree2, tree1.right))

    # 7
    tree1 = build_TreeNode([1])
    tree2 = copy.deepcopy(tree1)
    print(Solution().getTargetCopy(tree1, tree2, tree1))

    # 4
    tree1 = build_TreeNode([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
    tree2 = copy.deepcopy(tree1)
    print(Solution().getTargetCopy(tree1, tree2, tree1.right.right.right))

    # 5
    tree1 = build_TreeNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tree2 = copy.deepcopy(tree1)
    print(Solution().getTargetCopy(tree1, tree2, tree1.left.right))

    # 2
    tree1 = build_TreeNode([1, 2, None, 3])
    tree2 = copy.deepcopy(tree1)
    print(Solution().getTargetCopy(tree1, tree2, tree1.left))
