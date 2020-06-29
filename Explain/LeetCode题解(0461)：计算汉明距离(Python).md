# LeetCode题解(0461)：计算汉明距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hamming-distance/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(1)       | O(1)       | 40ms (69.51%) |
| Ans 2 (Python) | O(1)       | O(1)       | 44ms (44.88%) |
| Ans 3 (Python) | O(1)       | O(1)       | 36ms (87.80%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count("1")
```

解法二（移位统计距离）：

```python
def hammingDistance(self, x: int, y: int) -> int:
    n = x ^ y
    distance = 0
    while n:
        if n & 1 == 1:
            distance += 1
        n = n >> 1
    return distance
```

解法三（布莱恩·克尼根算法）：

```python
def hammingDistance(self, x: int, y: int) -> int:
    n = x ^ y
    distance = 0
    while n:
        distance += 1
        n = n & (n - 1)
    return distance
```