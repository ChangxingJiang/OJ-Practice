from toolkit import TreeNode, build_TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    tree = build_TreeNode([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
    print(Solution().increasingBST(tree))
    # [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
