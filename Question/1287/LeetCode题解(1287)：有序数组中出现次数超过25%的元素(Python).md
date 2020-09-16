# LeetCode题解(1287)：有序数组中出现次数超过25%的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 116ms (70.61%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 104ms (97.31%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findSpecialInteger(self, arr: List[int]) -> int:
    idx = 0
    for i in range(len(arr)):
        if arr[i] != arr[idx]:
            if i - idx > len(arr) // 4:
                return arr[idx]
            else:
                idx = i
    else:
        return arr[idx]
```

解法二（四次二分查找法）：

```python
def findSpecialInteger(self, arr: List[int]) -> int:
    span = len(arr) // 4 + 1
    for i in range(0, len(arr), span):
        if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) >= span:
            return arr[i]
    return -1
```