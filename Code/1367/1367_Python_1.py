from toolkit import ListNode
from toolkit import TreeNode, build_TreeNode


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def helper(node, maybe):
            # 处理当前节点为空的情况
            if not node:
                return False

            new_maybe = []
            for m in maybe:
                if node.val == m.val:
                    if m.next is None:
                        return True
                    new_maybe.append(m.next)
            if node.val == head.val:
                if head.next is None:
                    return True
                new_maybe.append(head.next)

            return helper(node.left, new_maybe) or helper(node.right, new_maybe)

        return helper(root, [])


if __name__ == "__main__":
    print(Solution().isSubPath(
        ListNode([4, 2, 8]),
        build_TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # True

    print(Solution().isSubPath(
        ListNode([1, 4, 2, 6]),
        build_TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # True

    print(Solution().isSubPath(
        ListNode([1, 4, 2, 6, 8]),
        build_TreeNode([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))  # False

    print(Solution().isSubPath(
        ListNode([1, 10]),
        build_TreeNode([1, None, 1, 10, 1, 9])
    ))  # True
