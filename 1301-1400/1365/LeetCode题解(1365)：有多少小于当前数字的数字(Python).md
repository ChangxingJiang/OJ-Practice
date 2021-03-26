# LeetCode题解(1365)：有多少小于当前数字的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)（简单）

题目1331延伸

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 40ms (96.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    s = sorted(nums)
    hashmap = {}
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = i

    ans = []
    for n in nums:
        ans.append(hashmap[n])
    return ans
```