# LeetCode题解(0670)：最大交换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-swap/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 52ms (6.21%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(ch) for ch in str(num)]
        for i in range(len(num)):
            max_idx, mav_val = i, num[i]
            for j in range(i + 1, len(num)):
                if mav_val <= num[j] and num[i] < num[j]:
                    max_idx, mav_val = j, num[j]
            if max_idx != i:
                num[i], num[max_idx] = num[max_idx], num[i]
                break
        return int("".join(str(i) for i in num))
```

