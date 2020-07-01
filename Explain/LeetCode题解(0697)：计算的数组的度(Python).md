# LeetCode题解(0697)：计算的数组的度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/degree-of-an-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 3100ms (9.75%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 264ms (94.86%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findShortestSubArray(self, nums: List[int]) -> int:
    hashmap = {}
    for n in nums:
        if n in hashmap:
            hashmap[n] += 1
        else:
            hashmap[n] = 1
    maximum = max(hashmap.values())

    max_nums = []
    for key, value in hashmap.items():
        if value == maximum:
            max_nums.append(key)

    minimum = len(nums)
    for max_num in max_nums:
        idx1 = 0
        idx2 = len(nums) - 1
        while nums[idx1] != max_num:
            idx1 += 1
        while nums[idx2] != max_num:
            idx2 -= 1
        size = idx2 - idx1 + 1
        minimum = min(minimum, size)

    return minimum
```

解法二（记录元素的左右位置）：

```python
def findShortestSubArray(self, nums: List[int]) -> int:
    left, right, count = {}, {}, {}
    for i in range(len(nums)):
        n = nums[i]
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
        if n not in left:
            left[n] = i
        right[n] = i

    degree = max(count.values())
    ans = len(nums)

    for n in count:
        if count[n] == degree:
            ans = min(ans, right[n] - left[n] + 1)

    return ans
```