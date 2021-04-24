# LeetCode题解(1780)：判断一个数字是否可以表示成三的幂的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-number-is-a-sum-of-powers-of-three/)（中等）

标签：数学、递归、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (64.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            mod = n % 3
            if mod == 0:
                n //= 3
            elif mod == 1:
                n -= 1
                n //= 3
            else:
                return False
        return True
```

