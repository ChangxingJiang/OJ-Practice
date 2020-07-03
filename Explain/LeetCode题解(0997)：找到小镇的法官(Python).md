# LeetCode题解(0997)：找到小镇的法官(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-town-judge/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+T)$   | $O(N)$     | 108ms (90.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findJudge(self, N: int, trust: List[List[int]]) -> int:
    maybe = [0 for _ in range(N)]
    for t in trust:
        maybe[t[0] - 1] -= 1
        maybe[t[1] - 1] += 1
    for i in range(N):
        if maybe[i] == N-1:
            return i+1
    else:
        return -1
```