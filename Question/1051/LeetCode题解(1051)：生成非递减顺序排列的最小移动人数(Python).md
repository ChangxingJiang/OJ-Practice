# LeetCode题解(1051)：生成非递减顺序排列的最小移动人数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/height-checker/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 32ms (96.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
def heightChecker(self, heights: List[int]) -> int:
    ans = 0
    for (x, y) in zip(heights, sorted(heights)):
        if x != y:
            ans += 1
    return ans
```