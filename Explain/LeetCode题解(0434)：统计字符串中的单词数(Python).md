# LeetCode题解(0434)：统计字符串中的单词数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-segments-in-a-string/)（简单）

| 解法           | 执行用时                      |
| -------------- | ----------------------------- |
| Ans 1 (Python) | 36ms (86.67%) - 56ms (6.24%)  |
| Ans 2 (Python) | 36ms (86.67%) - 40ms (66.99%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```Python
def countSegments(self, s: str) -> int:
    return sum([1 for i in re.split(" +", s) if len(i) > 0])
```

解法二（遍历）：

```python
def countSegments(self, s: str) -> int:
    not_space = False
    ans = 0
    for c in s:
        if c != " ":
            not_space = True
        else:
            if not_space:
                ans += 1
                not_space = False
    ans += not_space
    return ans
```