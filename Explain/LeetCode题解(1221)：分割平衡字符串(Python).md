# LeetCode题解(1221)：分割平衡字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (96.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def balancedStringSplit(self, s: str) -> int:
    num = 0
    ans = 0
    for c in s:
        if c == "L":
            num -= 1
        if c == "R":
            num += 1
        if num == 0:
            ans += 1
    return ans
```