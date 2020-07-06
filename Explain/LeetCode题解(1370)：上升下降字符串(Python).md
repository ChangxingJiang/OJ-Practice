# LeetCode题解(1370)：上升下降字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/increasing-decreasing-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (88.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def sortString(self, s: str) -> str:
    count = collections.Counter(s)
    ans = ""
    while len(ans) < len(s):
        sub = ""
        for k in list("abcdefghijklmnopqrstuvwxyz"):
            if count[k] > 0:
                sub += k
                count[k] -= 1
        ans += sub
        sub = ""
        for k in list("zyxwvutsrqponmlkjihgfedcba"):
            if count[k] > 0:
                sub += k
                count[k] -= 1
        ans += sub
    return ans
```