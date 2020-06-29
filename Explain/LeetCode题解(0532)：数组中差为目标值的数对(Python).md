# LeetCode题解(0532)：数组中差为目标值的数对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 192ms (38.03%) |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针遍历）：

```python
def findPairs(self, nums: List[int], k: int) -> int:
    if len(nums) < 2:
        return 0

    nums.sort()

    idx1 = 0
    idx2 = 1
    ans = set()
    while idx1 < len(nums) - 1 and idx2 <= len(nums) - 1:
        if idx1 == idx2:
            idx2 += 1
        s = nums[idx2] - nums[idx1]
        if s > k:
            idx1 += 1
        elif s < k:
            idx2 += 1
        else:
            ans.add((nums[idx1], nums[idx2]))
            idx1 += 1

    return len(ans)
```

解法二（暴力解法）：

```python
def findPairs(self, nums: List[int], k: int) -> int:
    if k <0:
        return 0
    
    ans = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] - nums[j] == k:
                ans.add((nums[i], nums[j]))
            elif nums[j] - nums[i] == k:
                ans.add((nums[j], nums[i]))
    return len(ans)
```