# LeetCode题解(0949)：给定的数字能组成的最大时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-time-for-given-digits/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (95.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（枚举所有可能的时间）：

```python
def largestTimeFromDigits(self, A: List[int]) -> str:
    ans = []
    for maybe in itertools.permutations(A, 4):
        hour = maybe[0] * 10 + maybe[1]
        minute = maybe[2] * 10 + maybe[3]
        if hour >= 24:
            continue
        elif minute >= 60:
            continue
        ans.append(str(hour).zfill(2) + ":" + str(minute).zfill(2))

    if len(ans) == 0:
        return ""
    else:
        return sorted(ans, reverse=True)[0]
```