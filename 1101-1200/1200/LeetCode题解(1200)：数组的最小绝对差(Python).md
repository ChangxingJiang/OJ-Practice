# LeetCode题解(1200)：数组的最小绝对差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-absolute-difference/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 396ms (99.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()

    min_num = float("inf")
    min_list = []
    for i in range(len(arr) - 1):
        d = arr[i + 1] - arr[i]
        if d < min_num:
            min_num = d
            min_list = [[arr[i], arr[i + 1]]]
        elif d == min_num:
            min_list.append([arr[i], arr[i + 1]])
    return min_list
```