from typing import List

from toolkit import TreeNode


class Solution:
    def __init__(self):
        self.memo = {
            0: [],
            1: [TreeNode(0)]
        }

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N not in self.memo:
            ans = []
            for left in range(1, N, 2):
                right = N - left - 1
                for left_tree in self.allPossibleFBT(left):
                    for right_tree in self.allPossibleFBT(right):
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        ans.append(root)
            self.memo[N] = ans

        return self.memo[N]


if __name__ == "__main__":
    # [
    #   [0,0,0,null,null,0,0,null,null,0,0],
    #   [0,0,0,null,null,0,0,0,0],
    #   [0,0,0,0,0,0,0],
    #   [0,0,0,0,0,null,null,null,null,0,0],
    #   [0,0,0,0,0,null,null,0,0]
    # ]
    print(Solution().allPossibleFBT(7))
