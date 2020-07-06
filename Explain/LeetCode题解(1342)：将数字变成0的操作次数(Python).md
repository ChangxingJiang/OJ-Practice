# LeetCode题解(1342)：将数字变成0的操作次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (74.58%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（每一次要不进行一次右移位，要不移除一个个位的1）：

```python
def numberOfSteps(self, num: int) -> int:
    num = bin(num)[2:]
    return len(num) + num.count("1") - 1
```