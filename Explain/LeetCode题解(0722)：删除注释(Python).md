# LeetCode题解(0722)：删除代码中的注释内容(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-comments/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (72.56%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (72.56%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        removing = False  # 是否在被多行屏蔽的情况下
        ans = []
        idx = 0
        in_line = False
        while idx < len(source):
            line = source[idx]  # 读取当前行信息
            if removing:
                if "*/" in line:
                    removing = False
                    source[idx] = line[line.index("*/") + 2:]
                else:
                    idx += 1
            else:
                N = len(line)
                idx_1 = line.index("//") if "//" in line else N
                idx_2 = line.index("/*") if "/*" in line else N
                if idx_1 < idx_2 and "//" in line:
                    if in_line and ans:
                        content = ans.pop() + line[:line.index("//")]
                        in_line = False
                    else:
                        content = line[:line.index("//")]
                    if content:
                        ans.append(content)
                    idx += 1
                elif idx_1 > idx_2:
                    if in_line and ans:
                        ans.append(ans.pop() + line[:line.index("/*")])
                    else:
                        ans.append(line[:line.index("/*")])
                    source[idx] = line[line.index("/*") + 2:]
                    removing = True
                    in_line = True
                else:
                    if in_line and ans:
                        content = ans.pop() + line
                        in_line = False
                    else:
                        content = line
                    if content:
                        ans.append(content)
                    idx += 1
        return ans
```

解法二（整理解法一代码）：

```python
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        is_block = False  # 是否在被多行屏蔽的情况下
        in_line = False  # 当前是否换行

        ans = []

        idx = 0
        while idx < len(source):
            line = source[idx]  # 读取当前行信息

            if is_block:  # 处理当前正在多行屏蔽的情况下
                if "*/" in line:
                    is_block = False
                    source[idx] = line[line.index("*/") + 2:]
                else:
                    idx += 1
            else:
                content = ans.pop() if in_line and ans else ""  # 当前行结果

                idx_1 = line.index("//") if "//" in line else float("inf")
                idx_2 = line.index("/*") if "/*" in line else float("inf")

                if idx_1 < idx_2:
                    in_line = False
                    content += line[:line.index("//")]
                    if content:
                        ans.append(content)
                    idx += 1
                elif idx_1 > idx_2:
                    is_block, in_line = True, True
                    ans.append(content + line[:line.index("/*")])
                    source[idx] = line[line.index("/*") + 2:]
                else:
                    in_line = False
                    content += line
                    if content:
                        ans.append(content)
                    idx += 1
        return ans
```