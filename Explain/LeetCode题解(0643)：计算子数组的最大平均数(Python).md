# LeetCode题解(0643)：计算子数组的最大平均数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-average-subarray-i/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 超出时间限制    |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 1020ms (91.29%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 1096ms (62.83%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    maximum = float("-inf")
    for i in range(len(nums) - k + 1):
        n = sum(nums[i:i + k])
        maximum = max(maximum, n)
    return maximum / k
```

解法二（累计求和）：

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    maximum = [sum(nums[0:k])] * (len(nums) - k + 1)
    for i in range(0, len(nums) - k):
        maximum[i] = maximum[i - 1] - nums[i] + nums[i + k]
    return max(maximum) / k
```

解法三（滑动最大值窗口）：

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    maximum = now = sum(nums[0:k])
    for i in range(0, len(nums) - k):
        now = now - nums[i] + nums[i + k]
        maximum = max(maximum, now)
    return maximum / k
```