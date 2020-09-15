from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        already_finish = False
        queue = [root]
        for node in queue:
            if node.left:
                if already_finish:
                    return False
                queue.append(node.left)
            else:
                already_finish = True
            if node.right:
                if already_finish:
                    return False
                queue.append(node.right)
            else:
                already_finish = True

        return True


if __name__ == "__main__":
    print(Solution().isCompleteTree(build_TreeNode([1, 2, 3, 4, 5, 6])))  # True
    print(Solution().isCompleteTree(build_TreeNode([1, 2, 3, 4, 5, None, 7])))  # False
