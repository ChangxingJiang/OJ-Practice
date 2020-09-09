from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, 0])))  # 1
    print(Solution().minCameraCover(build_TreeNode([0, 0, None, 0, None, 0, None, None, 0])))  # 2
