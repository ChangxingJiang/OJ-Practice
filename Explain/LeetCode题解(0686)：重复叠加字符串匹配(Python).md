# LeetCode题解(0686)：重复叠加字符串匹配(Python)

题目：[原题链接](https://leetcode-cn.com/problems/repeated-string-match/)（简单）

| 解法           | 时间复杂度 | 空间复杂度     | 执行用时       |
| -------------- | ---------- | -------------- | -------------- |
| Ans 1 (Python) | --     | $O(N)$  |     108ms (83.43%)           |
| Ans 2 (Python) | --         | $O(N)$         | 32ms (100.00%) |
| Ans 3 (Python) |            |                |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def repeatedStringMatch(self, A: str, B: str) -> int:
    times = len(B) // len(A) + 2
    n = A * times
    if B in n:
        n = A * (times - 1)
        if B in n:
            n = A * (times - 2)
            if B in n:
                return times - 2
            else:
                return times - 1
        else:
            return times
    else:
        return -1
```

解法二（增加前置判断）：

![LeetCode题解(0686)：截图1.png](LeetCode题解(0686)：截图1.png)

```python
ef repeatedStringMatch(self, A: str, B: str) -> int:
    if not set(B).issubset(set(A)):
        return -1
    size = len(B) // len(A)
    for i in range(size, size + 3):
        if B in A * i:
            return i
    return -1
```