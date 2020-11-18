# LeetCode题解(1481)：不同整数的最少数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/least-number-of-unique-integers-after-k-removals/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (91%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        num_list = list(sorted(count.values()))
        size = len(num_list)

        ans = size

        for i in range(size):
            if k >= num_list[i]:
                ans -= 1
                k -= num_list[i]
            else:
                return ans

        return 0
```