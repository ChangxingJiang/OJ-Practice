# LeetCode题解(1403)：非递增顺序的最小子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 40ms (92.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
def minSubsequence(self, nums: List[int]) -> List[int]:
    nums.sort(reverse=True)
    total = sum(nums)
    ans = []
    now = 0
    idx = 0
    while idx < len(nums) and now <= total - now:
        now += nums[idx]
        ans.append(nums[idx])
        idx += 1
    return ans
```

