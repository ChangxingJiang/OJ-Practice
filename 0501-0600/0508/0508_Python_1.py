import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.count = collections.Counter()

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def recursor(node):
            if not node:
                return 0
            left_val = recursor(node.left)
            right_val = recursor(node.right)
            node_val = node.val + left_val + right_val
            self.count[node_val] += 1
            return node_val

        recursor(root)

        ans = []
        max_val = None

        for node in self.count.most_common():
            if max_val is None:
                max_val = node[1]
                ans.append(node[0])
            elif node[1] == max_val:
                ans.append(node[0])
            else:
                break

        return ans


if __name__ == "__main__":
    print(Solution().findFrequentTreeSum(build_TreeNode([5, 2, -3])))  # [2,-3,4]
    print(Solution().findFrequentTreeSum(build_TreeNode([5, 2, -5])))  # [2]
