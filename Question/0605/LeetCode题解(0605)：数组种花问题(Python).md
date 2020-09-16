# LeetCode题解(0605)：数组种花问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-place-flowers/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 196ms (88.08%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 200ms (79.05%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（计算空间）：

```python
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    k = 1
    for b in flowerbed:
        if b == 0:
            k += 1
        else:
            if k > 0:
                n -= (k - 1) // 2
            k = 0
    else:
        if k > 0:
            n -= k // 2
    return n <= 0
```

解法二（直接种花）：

```python
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 \
                and (i == 0 or flowerbed[i - 1] == 0) \
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n <= 0:
                return True
    else:
        return n <= 0
```