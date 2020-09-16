# LeetCode题解(Offer17)：打印从1到最大的n位数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (83.23%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
```