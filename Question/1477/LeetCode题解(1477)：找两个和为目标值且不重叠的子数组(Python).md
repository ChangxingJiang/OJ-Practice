# LeetCode题解(1477)：找两个和为目标值且不重叠的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)（中等）

标签：数组、滑动窗口、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 316ms (94%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（滑动窗口）：

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 符合条件的数组
        ans_list = []

        # 滑动窗口需要符合条件的数组
        # O(N)
        size = len(arr)
        left, right = 0, 0  # 滑动窗口的左右边界
        window = 0  # 滑动窗口中的和
        while right <= size:
            # 滑动窗口
            if window < target:
                if right < size:
                    window += arr[right]
                    right += 1
                else:
                    break
            else:
                window -= arr[left]
                left += 1

            # 判断窗口值是否符合要求
            if window == target:
                ans_list.append((right - left, left, right - 1))

        # 处理没有符合的要求的情况
        if len(ans_list) < 2:
            return -1

        # 排序所有符合要求的窗口值（窗口宽度 -> 窗口左侧边框）
        # O(NlogN)
        ans_list.sort()

        # print(ans_list)

        # 遍历窗口寻找结果
        # O(N^2)
        ans = float("inf")
        for i in range(len(ans_list)):
            first = ans_list[i]  # 第1个窗口的宽度
            if first[0] >= ans:
                break

            for j in range(i + 1, len(ans_list)):
                second = ans_list[j]
                if first[0] + second[0] >= ans:
                    break

                # 处理存在重叠的情况
                if first[1] <= second[1] <= first[2] or first[1] <= second[2] <= first[2]:
                    continue

                ans = min(ans, first[0] + second[0])

        return ans if ans <= size else -1
```