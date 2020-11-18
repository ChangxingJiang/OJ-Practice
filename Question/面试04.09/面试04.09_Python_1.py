from itertools import combinations
from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        elif root.left and root.right:
            ans = []
            left_list = self.BSTSequences(root.left)
            right_list = self.BSTSequences(root.right)
            for left in left_list:
                for right in right_list:
                    size = len(left) + len(right)
                    for p in combinations([i for i in range(size)], len(right)):
                        right_idx = set(p)
                        lst = [root.val]
                        i1, i2 = 0, 0
                        for i in range(size):
                            if i not in right_idx:
                                lst.append(left[i1])
                                i1 += 1
                            else:
                                lst.append(right[i2])
                                i2 += 1
                        ans.append(lst)
            return ans
        elif root.left:
            ans = []
            for lst in self.BSTSequences(root.left):
                ans.append([root.val] + lst)
            return ans
        elif root.right:
            ans = []
            for lst in self.BSTSequences(root.right):
                ans.append([root.val] + lst)
            return ans
        else:
            return [[root.val]]


if __name__ == "__main__":
    # [
    #    [2,1,3],
    #    [2,3,1]
    # ]
    print(Solution().BSTSequences(build_TreeNode([2, 1, 3])))

    # [[5,2,1,4,3],[5,2,4,1,3],[5,2,4,3,1]]
    print(Solution().BSTSequences(build_TreeNode([5, 2, None, 1, 4, None, None, 3])))
