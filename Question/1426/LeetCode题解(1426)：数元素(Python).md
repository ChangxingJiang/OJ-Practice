# LeetCode题解(1426)：数元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/counting-elements/)（简单）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (97.36%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0
        for n in arr:
            if n + 1 in arr_set:
                ans += 1
        return ans
```