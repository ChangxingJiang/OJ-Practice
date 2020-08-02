# LeetCode题解(0071)：简化文件路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/simplify-path/)（中等）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (98.36%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def simplifyPath(self, path: str) -> str:
    ans = []
    for p in path.split("/"):
        if p == ".." and ans:
            ans.pop()
        elif len(p) > 0 and p != "." and p != "..":
            ans.append(p)
    return "/" + "/".join(ans)
```