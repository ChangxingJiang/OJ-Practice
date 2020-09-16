# LeetCode题解(0561)：数组拆分使各对最小值的总和最大(Python)

题目：[原题链接](https://leetcode-cn.com/problems/array-partition-i/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 340ms (72.12%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（相当于升序排序后累加所有技术项）：

```python
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(0, len(nums), 2):
        ans += nums[i]
    return ans
```