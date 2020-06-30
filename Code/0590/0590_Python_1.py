from typing import List

from toolkit import Node, build_Node


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(node: "Node"):
            if node is None:
                return []
            if node.children is None:
                return [node.val]
            ans = []
            for child in node.children:
                ans += helper(child)
            ans += [node.val]
            return ans

        return helper(root)


if __name__ == "__main__":
    print(Solution().postorder(build_Node([1, None, 3, 2, 4, None, 5, 6])))  # [5,6,3,2,4,1]
