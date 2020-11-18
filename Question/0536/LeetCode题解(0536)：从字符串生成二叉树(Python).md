# LeetCode题解(0536)：从字符串生成二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-binary-tree-from-string/)（中等）

标签：树、二叉树、字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 140ms (34.94%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def is_number(ss):
            for cc in ss:
                if not cc.isnumeric() and not cc == "-":
                    return False
            return True

        if not s:
            return None

        lst = []
        for ch in s:
            if is_number(ch):
                if lst and is_number(lst[-1]):
                    lst[-1] += ch
                else:
                    lst.append(ch)
            else:
                lst.append(ch)

        print(lst)

        stack = [TreeNode(int(lst[0]))]
        i = 1
        while i < len(lst):
            if lst[i] == "(":
                new = TreeNode(int(lst[i + 1]))
                if not stack[-1].left:
                    stack[-1].left = new
                    stack.append(new)
                else:
                    stack[-1].right = new
                    stack.append(new)
                i += 2
            elif lst[i] == ")":
                stack.pop()
                i += 1

        return stack[0]
```