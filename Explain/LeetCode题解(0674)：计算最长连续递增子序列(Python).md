# LeetCode题解(0674)：计算最长连续递增子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 92ms (87.88%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 92ms (87.88%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findLengthOfLCIS(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    maximum = num = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            num += 1
            maximum = max(maximum, num)
        else:
            num = 1
    return maximum
```

解法二：

```python
def findLengthOfLCIS(self, nums: List[int]) -> int:
    ans = idx = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            idx = i
        ans = max(ans, i - idx + 1)
    return ans
```