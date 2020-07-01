# LeetCode题解(0704)：二分查找(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-search/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 296ms (92.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def search(self, nums: List[int], target: int) -> int:
    idx0 = 0
    idx1 = len(nums)
    while idx0 < idx1:
        mid = int((idx1 + idx0) / 2)
        if target < nums[mid]:
            idx1 = mid
        elif target > nums[mid]:
            idx0 = mid + 1
        else:
            return mid
    else:
        return -1
```