# LeetCode题解(0556)：计算调换整数的位使整数值大于当前值的最小值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/next-greater-element-iii/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (64.23%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = [int(ch) for ch in str(n)]
        now = []
        for i in range(len(lst) - 1, -1, -1):
            n = lst[i]
            if not now or now[-1] <= n:
                bisect.insort_left(now, n)
            else:
                this = now.pop(bisect.bisect_right(now, n))
                bisect.insort_left(now, n)
                ans = lst[:i] + [this] + now
                ans = int("".join([str(v) for v in ans]))
                return ans if ans < 2 ** 31 else -1
        return -1
```