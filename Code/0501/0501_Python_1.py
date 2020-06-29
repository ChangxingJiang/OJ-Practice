from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        hashmap = {}

        def helper(node):
            if node:
                if node.val in hashmap:
                    hashmap[node.val] += 1
                else:
                    hashmap[node.val] = 1
                return helper(node.left), helper(node.right)

        helper(root)
        maximum = max(hashmap.values())

        ans = []
        for key, value in hashmap.items():
            if value == maximum:
                ans.append(key)

        return ans


if __name__ == "__main__":
    print(Solution().findMode(build_TreeNode([1, None, 2, 2])))  # 2
