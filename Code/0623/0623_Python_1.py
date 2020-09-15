import collections

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # 处理d的值为1的情况
        if d == 1:
            ans = TreeNode(v)
            ans.left = root
            return ans

        d -= 1

        # 层序遍历树到目标行的上一行
        queue = collections.deque([root])
        while d > 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            d -= 1

        print(queue)

        # 增加新的一行
        for node in queue:
            if node.left:
                new_node = TreeNode(v)
                new_node.left = node.left
                node.left = new_node
            else:
                node.left = TreeNode(v)
            if node.right:
                new_node = TreeNode(v)
                new_node.right = node.right
                node.right = new_node
            else:
                node.right = TreeNode(v)

        return root


if __name__ == "__main__":
    # [4,1,1,2,None,None,6,3,1,5]
    print(Solution().addOneRow(build_TreeNode([4, 2, 6, 3, 1, 5]), 1, 2))

    # [1,2,3,4,null,null,null,5,5]
    print(Solution().addOneRow(build_TreeNode([1, 2, 3, 4]), 5, 4))
