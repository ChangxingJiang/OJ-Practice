# LeetCode题解(1198)：找出所有行中最小公共元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-smallest-common-element-in-all-rows/)（中等）

标签：哈希表、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogM)$ | $O(N)$     | 80ms (78.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        size1, size2 = len(mat), len(mat[0])

        hashmap = {i: 0 for i in range(size1)}
        now = [m[0] for m in mat]

        while len(set(now)) > 1:

            max_val = max(now)

            for i in range(size1):
                idx = bisect.bisect(mat[i], max_val, lo=hashmap[i])
                # print(mat[i], max_val, "->", idx - 1)
                if mat[i][idx - 1] == max_val:
                    hashmap[i] = idx - 1
                elif idx >= size2:
                    return -1
                else:
                    hashmap[i] = idx

            now = [mat[i][hashmap[i]] for i in range(size1)]

        return now[0]
```