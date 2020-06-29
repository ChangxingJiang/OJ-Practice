from toolkit import TreeNode, build_TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    # [3,4,5,5,4,None,7]
    print(Solution().mergeTrees(build_TreeNode([1, 3, 2, 5]),
                                build_TreeNode([2, 1, 3, None, 4, None, 7])))
