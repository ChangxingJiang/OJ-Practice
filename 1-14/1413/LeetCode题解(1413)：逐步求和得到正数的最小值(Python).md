# LeetCode题解(1413)：逐步求和得到正数的最小值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum/)（简单）

标签：简单数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (39.32%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (94.12%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def minStartValue(self, nums: List[int]) -> int:
    minimum = 0
    now = 0
    for n in nums:
        now += n
        minimum = min(minimum, now)
    return 1 - minimum
```

解法二：

```python
def minStartValue(self, nums: List[int]) -> int:
    ans = 1
    now = 1
    for n in nums:
        now += n
        if now < 1:
            ans += 1 - now
            now = 1
    return ans
```