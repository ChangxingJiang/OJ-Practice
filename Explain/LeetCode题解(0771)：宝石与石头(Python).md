# LeetCode题解(0771)：宝石与石头(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jewels-and-stones/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (90.10%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 52ms (14.87%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numJewelsInStones(self, J: str, S: str) -> int:
    ans = 0
    for j in J:
        ans += S.count(j)
    return ans
```

解法二：

```python
def numJewelsInStones(self, J: str, S: str) -> int:
    ans = 0
    for s in S:
        if s in J:
            ans += 1
    return ans
```