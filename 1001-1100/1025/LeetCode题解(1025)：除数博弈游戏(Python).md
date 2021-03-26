# LeetCode题解(1025)：除数博弈游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/divisor-game/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 48ms (47.30%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 28ms (99.56%) |
| Ans 3 (Python) | $O(1)$     | $O(1)$     | 36ms (91.69%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

```python
def divisorGame(self, N: int) -> bool:
    situations = {
        1: False
    }
    for i in range(2, N + 1):
        chooses = {i - 1}
        for k in (2, i // 2 + 1):
            if i % k == 0 and 0 < i - k < i:
                chooses.add(i - k)
        situations[i] = not all(situations[choose] for choose in chooses)

    return situations[N]
```

解法二：

```python
def divisorGame(self, N: int) -> bool:
    return N % 2 == 0
```

解法三（位运算）：

```python
def divisorGame(self, N: int) -> bool:
    return not N & 1
```