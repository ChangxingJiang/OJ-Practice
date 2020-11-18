# LeetCode题解(1537)：相互交汇的两个数组的最大得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/get-the-maximum-score/)（困难）

标签：数组、哈希表、双指针、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 132ms (97%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # 计算所有交叉路口（共存的值）
        # O(N1+N2)
        sets1 = set(nums1)
        cross = [n for n in nums2 if n in sets1]

        # 遍历计算两个数组到各个交叉路口的路径和
        # O(N1+N2)
        distances_1 = []
        idx = 0
        now = 0
        for num1 in nums1:
            if idx < len(cross) and num1 == cross[idx]:
                distances_1.append(now)
                now = 0
                idx += 1
            else:
                now += num1
        distances_1.append(now)

        distances_2 = []
        idx = 0
        now = 0
        for num2 in nums2:
            if idx < len(cross) and num2 == cross[idx]:
                distances_2.append(now)
                now = 0
                idx += 1
            else:
                now += num2
        distances_2.append(now)

        # 计算最终的最大值
        # O(CROSS) CROSS为交汇点数量
        ans = sum(cross)
        for i in range(len(distances_1)):
            ans += max(distances_1[i], distances_2[i])

        return ans % (10 ** 9 + 7)
```