# LeetCode题解(0057)：向区间列表中插入区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-interval/)（困难）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (93.88%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 计算当前新区间位置
        # 时间:O(N) 空间:O(N)
        left_new, right_new = newInterval
        left_interval, right_interval, inner_interval = [], [], set()  # 新区间的左右边缘所在的区间
        for left, right in intervals:
            # 包含新区间的左侧边缘
            if left <= left_new <= right:
                left_interval = [left, right]

            # 包含新区间的右侧边缘
            if left <= right_new <= right:
                right_interval = [left, right]

            # 被新区间包含
            if left_new <= left <= right <= right_new:
                inner_interval.add((left, right))

        # 处理新区间没有与老区间相交的情况
        # O(N)
        if not left_interval and not right_interval and not inner_interval:
            ans = []
            already_add = False
            for left, right in intervals:
                if not already_add and right_new < left:
                    already_add = True
                    ans.append([left_new, right_new])
                ans.append([left, right])
            if not already_add:
                ans.append([left_new, right_new])
            return ans

        # 处理新区间没有与老区间相交，但是被老区间包含的情况
        # O(N)
        if not left_interval and not right_interval and inner_interval:
            ans = []
            already_add = False
            for left, right in intervals:
                if (left, right) in inner_interval:
                    if not already_add:
                        already_add = True
                        ans.append([left_new, right_new])
                else:
                    ans.append([left, right])
            if not already_add:
                ans.append([left_new, right_new])
            return ans

        # 处理新区间被老区间包含的情况
        # O(1)
        if left_interval == right_interval:
            return intervals

        # 处理新区间与老区间相交的情况
        # O(N)
        ans = []
        for left, right in intervals:
            # 处理包含新区间的左侧边缘
            if [left, right] == left_interval:
                ans.append([left, right_new])

            # 处理包含新区间的右侧边缘
            elif [left, right] == right_interval:
                if ans and ans[-1][1] >= left_new:
                    ans[-1][1] = right
                else:
                    ans.append([left_new, right])

            # 处理被新区间包含
            elif (left, right) in inner_interval:
                if not ans or ans[-1][1] != right_new:
                    ans.append([left_new, right_new])

            else:
                ans.append([left, right])

        return ans
```

