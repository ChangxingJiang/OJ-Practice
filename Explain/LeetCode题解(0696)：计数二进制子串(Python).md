# LeetCode题解(0696)：计数二进制子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-binary-substrings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 252ms (42.00%)  |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 104ms (100.00%) |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def countBinarySubstrings(self, s: str) -> int:
    num0 = 0
    num1 = 0
    ans = 0
    for i in range(len(s)):
        n = s[i]
        if i > 0 and s[i] != s[i - 1]:
            if s[i] == "0":
                num0 = 0
            else:
                num1 = 0
        if n == "1":
            if num0 > 0:
                ans += 1
                num0 -= 1
            num1 += 1
        elif n == "0":
            if num1 > 0:
                ans += 1
                num1 -= 1
            num0 += 1
    return ans
```

解法二（减少判断次数）：

![LeetCode题解(0696)：截图1](LeetCode题解(0696)：截图1.png)

```python
def countBinarySubstrings(self, s: str) -> int:
    pre = 0
    count = 1
    curr = s[0]
    ans = 0
    for n in s[1:]:
        if n == curr:
            count += 1
        else:
            pre = count
            count = 1
            curr = n
        if pre >= count:
            ans += 1
    return ans
```