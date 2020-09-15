from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if not root:
            return []
        if root.val != voyage[0]:
            return [-1]

        if root.left and root.right:
            if root.left.val == voyage[1]:
                if root.right.val not in voyage[2:]:
                    return [-1]
                idx = voyage.index(root.right.val)
                left = self.flipMatchVoyage(root.left, voyage[1:idx])
                right = self.flipMatchVoyage(root.right, voyage[idx:])
                if left == [-1] or right == [-1]:
                    return [-1]
                else:
                    return left + right
            elif root.right.val == voyage[1]:
                if root.left.val not in voyage[2:]:
                    return [-1]
                idx = voyage.index(root.left.val)
                right = self.flipMatchVoyage(root.right, voyage[1:idx])
                left = self.flipMatchVoyage(root.left, voyage[idx:])
                if left == [-1] or right == [-1]:
                    return [-1]
                else:
                    return [root.val] + left + right

            else:
                return [-1]

        elif root.left:
            if root.left.val == voyage[1]:
                return self.flipMatchVoyage(root.left, voyage[1:])
            else:
                return [-1]

        elif root.right:
            if root.right.val == voyage[1]:
                return self.flipMatchVoyage(root.right, voyage[1:])
            else:
                return [-1]

        else:
            if len(voyage) == 1:
                return []
            else:
                return [-1]


if __name__ == "__main__":
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2]), [2, 1]))  # [-1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 3, 2]))  # [1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 2, 3]))  # []
