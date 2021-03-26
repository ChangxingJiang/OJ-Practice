# LeetCode题解(0388)：文件的最长绝对路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-absolute-file-path/)（中等）

标签：栈、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (7.47%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")

        ans = 0

        stack = []  # 当前路径栈
        for line in lines:
            num = line.count("\t")
            while len(stack) > num:
                stack.pop()
                
            name = line.replace("\t", "")

            # 处理当前为文件的情况
            if "." in line:
                ans = max(ans, sum(len(n) for n in stack) + len(stack) + len(name))
            else:
                stack.append(name)

        return ans
```

