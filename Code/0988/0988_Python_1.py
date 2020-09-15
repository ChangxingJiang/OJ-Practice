from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def smallestFromLeaf(self, root: TreeNode, now="") -> str:
        if not root:
            return ""
        ch = chr(97 + root.val)
        if root.left and root.right:
            left = self.smallestFromLeaf(root.left, ch + now)
            right = self.smallestFromLeaf(root.right, ch + now)
            return min(left, right)
        elif root.left:
            return self.smallestFromLeaf(root.left, ch + now)
        elif root.right:
            return self.smallestFromLeaf(root.right, ch + now)
        else:
            return ch + now


if __name__ == "__main__":
    # "dba"
    print(Solution().smallestFromLeaf(build_TreeNode([0, 1, 2, 3, 4, 3, 4])))

    # "adz"
    print(Solution().smallestFromLeaf(build_TreeNode([25, 1, 3, 1, 3, 0, 2])))

    # "abc"
    print(Solution().smallestFromLeaf(build_TreeNode([2, 2, 1, None, 1, 0, None, 0])))

    # "bae"
    print(Solution().smallestFromLeaf(build_TreeNode([4, 0, 1, 1])))

    # "ababz"
    print(Solution().smallestFromLeaf(build_TreeNode([25, 1, None, 0, 0, 1, None, None, None, 0])))
