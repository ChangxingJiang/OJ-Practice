from collections import deque

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            if level % 2 == 0:
                last_val = float("-inf")
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.val % 2 == 0:
                        return False
                    if node.val <= last_val:
                        return False
                    last_val = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            else:
                last_val = float("inf")
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.val % 2 == 1:
                        return False
                    if node.val >= last_val:
                        return False
                    last_val = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            level += 1

        return True


if __name__ == "__main__":
    print(Solution().isEvenOddTree(build_TreeNode([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2])))  # True
    print(Solution().isEvenOddTree(build_TreeNode([5, 4, 2, 3, 3, 7])))  # False
    print(Solution().isEvenOddTree(build_TreeNode([5, 9, 1, 3, 5, 7])))  # False
    print(Solution().isEvenOddTree(build_TreeNode([1])))  # True
    print(Solution().isEvenOddTree(build_TreeNode([11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17])))  # True
