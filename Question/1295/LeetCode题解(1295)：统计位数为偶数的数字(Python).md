# LeetCode题解(1295)：统计位数为偶数的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (98.58%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findNumbers(self, nums: List[int]) -> int:
    ans = 0
    for n in nums:
        bit = True
        while n > 0:
            n = n // 10
            bit = not bit
        ans += bit
    return ans
```