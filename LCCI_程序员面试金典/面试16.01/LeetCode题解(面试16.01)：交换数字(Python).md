# LeetCode题解(面试16.01)：交换数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swap-numbers-lcci/)（中等）

标签：位运算、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (81.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[1] ^ numbers[0]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers
```