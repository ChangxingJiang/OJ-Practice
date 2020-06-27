# LeetCode题解(0374)：猜数字大小游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/guess-number-higher-or-lower/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(logn)    | O(1)       | 36ms (84.82%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（二分查找）：

```python
def guessNumber(self, n: int) -> int:
    s = 0
    while True:
        m = (s + n) // 2
        ans = guess(m)
        if ans == -1:
            n = m - 1
        elif ans == 1:
            s = m + 1
        else:
            return m
```