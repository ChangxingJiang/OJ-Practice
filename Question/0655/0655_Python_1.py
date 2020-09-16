import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # 生成包含None的层序遍历的结果
        lst = []
        queue = collections.deque([root])
        while True:
            now_val = []
            have_find = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val != "":
                    have_find = True
                    now_val.append(str(node.val))
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(TreeNode(""))
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(TreeNode(""))
                else:
                    now_val.append("")
                    queue.append(TreeNode(""))
                    queue.append(TreeNode(""))
            if not have_find:
                break
            else:
                lst.append(now_val)

        # 将结果转换为输出格式
        height = len(lst)  # 二叉树的高度
        length = 2 ** height - 1  # 输出结果的宽度
        ans = []
        for i in range(height):
            line = [""] * length
            for j in range(len(lst[i])):
                idx = (2 * (j + 1) - 1) * (2 ** (height - (i + 1))) - 1
                line[idx] = lst[i][j]
            ans.append(line)

        return ans


if __name__ == "__main__":
    # [["", "1", ""],
    #  ["2", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2])))

    # [["", "", "", "1", "", "", ""],
    #  ["", "2", "", "", "", "3", ""],
    #  ["", "", "4", "", "", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2, 3, None, 4])))

    # [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
    #  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
    #  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
    #  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
    print(Solution().printTree(build_TreeNode([1, 2, 5, 3, None, None, None, 4])))
