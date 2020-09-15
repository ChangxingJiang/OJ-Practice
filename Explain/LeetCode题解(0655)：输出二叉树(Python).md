# LeetCode题解(0655)：依据指定规则将二叉树输出为文本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/print-binary-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (81.02%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
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
```