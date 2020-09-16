from typing import List

from toolkit import TreeNode


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre:
            root = TreeNode(pre[0])

            if len(pre) == 1:
                return root

            idx = post.index(pre[1]) + 1  # 左子树节点数量

            root.left = self.constructFromPrePost(pre[1:idx + 1], post[:idx])
            root.right = self.constructFromPrePost(pre[idx + 1:], post[idx:-1])

            return root


if __name__ == "__main__":
    # [1,2,3,4,5,6,7]
    print(Solution().constructFromPrePost(pre=[1, 2, 4, 5, 3, 6, 7], post=[4, 5, 2, 6, 7, 3, 1]))

    # [2,1] 或 [2,None,1]
    print(Solution().constructFromPrePost(pre=[2, 1], post=[1, 2]))
