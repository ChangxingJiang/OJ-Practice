# LeetCode题解(Offer59I)：计算数组中滑动窗口的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)（简单）

标签：数组、队列、滑动窗口

| 解法           | 时间复杂度                                              | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 平均时间复杂度 = $O(N)$ ; 最坏时间复杂度 = $O((N-K)×K)$ | $O(K)$     | 56ms (99.27%) |
| Ans 2 (Python) | $O(N)$                                                  | $O(K)$     | 68ms (91.03%) |
| Ans 3 (Python) |                                                         |            |               |

解法一：

![LeetCode题解(Offer59I)：截图](LeetCode题解(Offer59I)：截图.png)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        ans = [max(nums[:k])]
        for i in range(k, len(nums)):
            if nums[i] >= ans[-1]:
                ans.append(nums[i])
            elif nums[i - k] == ans[-1]:
                ans.append(max(nums[i - k + 1:i + 1]))
            else:
                ans.append(ans[-1])

        return ans
```

解法二（双向队列）：

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 处理特殊情况
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        # 初始化滑动窗口队列
        queue = collections.deque()

        max_idx = 0

        for i in range(k):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if nums[i] > nums[max_idx]:
                max_idx = i

        ans = [nums[max_idx]]

        # 遍历并滑动窗口
        for i in range(k, len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            ans.append(nums[queue[0]])

        return ans
```



