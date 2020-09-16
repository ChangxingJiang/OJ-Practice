from typing import List

from toolkit import Node, build_Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def helper(node: 'Node'):
            if node is None:
                return []
            if node.children is None:
                return [node.val]
            ans = [node.val]
            for child in node.children:
                ans += helper(child)
            return ans

        return helper(root)


if __name__ == "__main__":
    print(Solution().preorder(build_Node([1, None, 3, 2, 4, None, 5, 6])))  # [1,3,5,6,2,4]
