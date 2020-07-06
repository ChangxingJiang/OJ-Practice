# LeetCode题解(1460)：通过翻转子数组使两个数组相等(Python)

题目：[原题链接](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (20.51%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (80.81%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    return len(collections.Counter(target) - collections.Counter(arr)) == 0
```

解法二：

```python
def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    return sorted(target) == sorted(arr)
```