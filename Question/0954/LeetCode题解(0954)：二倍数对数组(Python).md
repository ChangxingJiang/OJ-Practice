# LeetCode题解(0954)：二倍数对数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/array-of-doubled-pairs/)（中等）

标签：哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(AlogA)$ | $O(A)$     | 96ms (97.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)

        for k in sorted(count.keys()):
            if count[k] > 0:
                if k > 0:
                    if count[k * 2] >= count[k]:
                        count[k * 2] -= count[k]
                    else:
                        return False
                elif k < 0:
                    if count[k / 2] >= count[k]:
                        count[k / 2] -= count[k]
                    else:
                        return False
                else:  # k=0
                    if count[k] % 2 != 0:
                        return False

        return True
```