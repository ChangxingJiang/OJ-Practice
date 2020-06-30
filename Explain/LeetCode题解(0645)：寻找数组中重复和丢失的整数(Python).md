# LeetCode题解(0645)：寻找数组中重复和丢失的整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/set-mismatch/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 240ms (82.46%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(logN)$  | 248ms (73.20%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用哈希表）：

```
def findErrorNums(self, nums: List[int]) -> List[int]:
    arr = [0] * (len(nums) + 1)
    for n in nums:
        arr[n] += 1
    more = None
    lost = None
    for i in range(1, len(arr)):
        if arr[i] == 0:
            lost = i
        elif arr[i] == 2:
            more = i
    return [more, lost]
```

解法二（排序）：

```python
def findErrorNums(self, nums: List[int]) -> List[int]:
    nums.sort()
    more = -1
    lost = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            more = nums[i]
        elif nums[i] > nums[i - 1] + 1:
            lost = nums[i - 1] + 1
    return [more, lost if nums[-1] == len(nums) else len(nums)]
```