# LeetCode题解(0821)：到目标字符的最短距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-distance-to-a-character/)（简单）

与供暖器的题目类似

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (84.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双向遍历）：

```python
def shortestToChar(self, S: str, C: str) -> List[int]:
    ans = [float("inf") for _ in range(len(S))]
    for i in range(len(S)):
        if S[i] == C:
            ans[i] = 0
        elif i > 0:
            ans[i] = ans[i - 1] + 1
    for i in range(len(S) - 1, -1, -1):
        if S[i] == C:
            ans[i] = 0
        elif i < len(S) - 1:
            ans[i] = min(ans[i], ans[i + 1] + 1)
    return ans
```