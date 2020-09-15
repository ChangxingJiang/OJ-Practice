from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode, father=None, grandfather=None) -> int:
        if not root:
            return 0

        # 累计当前节点
        ans = 0
        if grandfather and grandfather.val % 2 == 0:
            ans += root.val

        grandfather = father
        father = root
        ans += self.sumEvenGrandparent(root.left, father, grandfather)
        ans += self.sumEvenGrandparent(root.right, father, grandfather)

        return ans


if __name__ == "__main__":
    # 18
    print(Solution().sumEvenGrandparent(build_TreeNode([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])))
