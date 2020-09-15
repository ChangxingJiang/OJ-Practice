# LeetCode题解(1028)：依据已知深度的先序遍历还原二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/)（困难）

标签：树、二叉树、深度优先搜索、字符串

| 解法           | 时间复杂度                     | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N×H)$ : 其中H为二叉树的深度 | $O(N×H)$   | 92ms (73.93%) |
| Ans 2 (Python) |                                |            |               |
| Ans 3 (Python) |                                |            |               |

解法一：

```python
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 将字符串格式转换为列表格式
        lst = []
        last = 0
        for i, ch in enumerate(S):
            if ch.isdigit() != S[last].isdigit():
                lst.append(S[last:i])
                last = i
        else:
            lst.append(S[last:])

        def build_tree(sub_lst, level=0):
            if sub_lst:
                sign = "-" * (level + 1)
                root = TreeNode(sub_lst[0])
                if sign in sub_lst[2:]:
                    idx = sub_lst[2:].index(sign) + 2
                    root.left = build_tree(sub_lst[2:idx], level + 1)
                    root.right = build_tree(sub_lst[idx + 1:], level + 1)
                else:
                    root.left = build_tree(sub_lst[2:], level + 1)
                return root

        return build_tree(lst)
```

