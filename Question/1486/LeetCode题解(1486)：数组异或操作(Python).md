# LeetCode题解(1486)：数组异或操作(Python)

题目：[原题链接](https://leetcode-cn.com/problems/xor-operation-in-an-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (71.92%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (71.92%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def xorOperation(self, n: int, start: int) -> int:
    nums = [start + 2 * i for i in range(n)]
    ans = 0
    for n in nums:
        ans = ans ^ n
    return ans
```

解法二：

```python
def xorOperation(self, n: int, start: int) -> int:
    ans = 0
    for i in range(n):
        ans = ans ^ (start + 2 * i)
    return ans
```