# LeetCode题解(1356)：根据数字二进制下1的数目排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (90.62%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
def sortByBits(self, arr: List[int]) -> List[int]:
    def helper(n):
        return bin(n).count("1"), n

    return sorted(arr, key=helper)
```