# LeetCode题解(0267)：回文排列II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-permutation-ii/)（中等）

标签：回溯算法、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 40ms (69.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
# ---------- 生成所有不同的全排列(0047题) ----------
def permuteUnique(nums):
    visited = set()
    ans = []
    now = []

    n = len(nums)

    def track_back():
        if len(now) == n:
            ans.append(now[:])
        tmp_set = set()
        for i in range(n):
            if i not in visited:
                if nums[i] in tmp_set:
                    continue
                tmp_set.add(nums[i])

                visited.add(i)
                now.append(nums[i])
                track_back()
                now.pop()
                visited.remove(i)

    track_back()

    return ans


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = collections.Counter(s)

        once = []
        twice = []

        for k, v in count.items():
            n, m = divmod(v, 2)
            if n:
                twice.extend([k] * n)
            if m:
                once.append(k)

        if len(once) > 1:
            return []

        ans = []
        for lst in permuteUnique(twice):
            ans.append("".join(lst + once + list(reversed(lst))))
        return ans
```