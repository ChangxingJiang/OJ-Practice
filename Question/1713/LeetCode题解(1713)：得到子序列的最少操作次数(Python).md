# LeetCode题解(1713)：得到子序列的最少操作次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/)（困难）

标签：二分查找、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 272ms (78.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        s1, s2 = len(target), len(arr)

        # 计算target中每个数值的位置
        count = {}
        for i in range(s1):
            count[target[i]] = i

        # 将arr转换为位置序列
        lst = []
        for i in range(s2):
            if arr[i] in count:
                lst.append(count[arr[i]])

        # 计算最长递增子序列
        queue = []
        for n in lst:
            if not queue or queue[-1] < n:
                queue.append(n)
            else:
                idx = bisect.bisect_right(queue, n)
                if idx == 0 or (queue[idx - 1] != n):
                    queue[idx] = n

        return s1 - len(queue)
```