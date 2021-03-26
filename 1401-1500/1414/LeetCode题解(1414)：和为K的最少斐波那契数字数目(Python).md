# LeetCode题解(1414)：和为K的最少斐波那契数字数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K)$     | $O(K)$     | 48ms (49.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
fibonacci_list = [1, 1]
while fibonacci_list[-2] + fibonacci_list[-1] <= 10 ** 9:
    fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans = 0
        for num in fibonacci_list[::-1]:
            if k >= num:
                ans += 1
                k -= num
        return ans
```

