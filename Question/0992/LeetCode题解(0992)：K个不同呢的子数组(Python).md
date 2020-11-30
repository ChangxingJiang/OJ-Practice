# LeetCode题解(0992)：K个不同呢的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/)（困难）

标签：哈希表、数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 724ms (44.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        i1, i2, i3 = 0, 0, 0  # 有K个不同的数组的开头，有K-1个不同的数组的开头，两个数组的结尾
        count1, count2 = collections.Counter(), collections.Counter()  # i1到i3的数组的情况，i2到i3的数组的情况

        ans = 0

        size = len(A)
        while i3 < size:
            # 移动数组右侧边缘指针
            ch3 = A[i3]
            count1[ch3] += 1
            count2[ch3] += 1

            # 移动i1到i3的数组左侧边缘指针
            while i1 <= i3 and len(count1) > K:
                ch1 = A[i1]
                count1[ch1] -= 1
                if count1[ch1] == 0:
                    del count1[ch1]
                i1 += 1

            # 移动i2到i3的数组左侧边缘指针
            while i2 <= i3 and len(count2) > K - 1:
                ch2 = A[i2]
                count2[ch2] -= 1
                if count2[ch2] == 0:
                    del count2[ch2]
                i2 += 1

            # 累加结果
            if len(count1) == K and len(count2) == K - 1:
                ans += i2 - i1

            i3 += 1

        return ans
```