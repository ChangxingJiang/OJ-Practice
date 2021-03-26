import collections

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 处理根节点为空的情况
        if not root:
            return 0

        ans = 0
        queue = collections.deque([(root, 1)])
        while queue:
            # 计算当前层的宽度
            min_idx = queue[0][1]
            max_idx = queue[-1][1]
            ans = max(ans, max_idx - min_idx + 1)

            # 寻找下一层的节点并将节点的值赋为节点坐标
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx * 2 - 1))
                if node.right:
                    queue.append((node.right, idx * 2))

        return ans


if __name__ == "__main__":
    # 4
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, 2, 5, 3, None, 9])))

    # 2
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, None, 5, 3])))

    # 8
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, 2, 5, None, None, 9, 6, None, None, 7])))
