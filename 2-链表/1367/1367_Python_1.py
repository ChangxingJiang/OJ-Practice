from toolkit import ListNode
from toolkit import TreeNode


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isSubPath(
        ListNode([4, 2, 8]),
        TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # True

    print(Solution().isSubPath(
        ListNode([1, 4, 2, 6]),
        TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # True

    print(Solution().isSubPath(
        ListNode([4, 2, 8]),
        TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # False
