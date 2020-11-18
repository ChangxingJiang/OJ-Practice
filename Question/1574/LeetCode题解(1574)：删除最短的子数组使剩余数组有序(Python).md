# LeetCode题解(1574)：删除最短的子数组使剩余数组有序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 128ms (40%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 寻找第1个和最后1个递减位置
        # O(N)
        first = -1  # 第1个递减位置(左侧元素坐标)
        last = -1  # 最后1个递减位置(左侧元素坐标)
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                if first == -1:
                    first = i - 1
                last = i - 1

        # 处理已经非递减的情况
        if first == -1 and last == -1:
            return 0

        # print(first, last)

        # 此时一定会被删除的范围：[first+1:last+1]
        ans_basic = last - first

        # 处理已经非递减的情况
        if arr[first] <= arr[last + 1]:
            return ans_basic

        # 处理尚未非递减的情况：在前后继续删除更多的元素
        # 先向后找到比当前值更大的情况
        right = []
        idx = last + 1
        while idx < len(arr) and arr[idx] < arr[first]:
            right.append(arr[idx])
            idx += 1

        ans_add = min(first + 1, len(right))

        # 向前检索，并依次将前面的结果在刚才匹配的后续元素中二分查找，寻找是否可以减少更少的元素
        # O(NlogN)
        idx = first - 1
        while idx >= 0:
            left_num = first - idx

            right_num = bisect.bisect_left(right, arr[idx])
            ans_add = min(ans_add, left_num + right_num)
            # print(right, arr[idx], "->", right_num)

            idx -= 1

            if right_num == 0:
                break

        return ans_basic + ans_add
```