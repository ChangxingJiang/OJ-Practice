# LeetCode题解(面试17.05)：字母与数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-longest-subarray-lcci/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $L(N)$     | 160ms (87.84%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic = {0: 0}
        count = 0
        ans_idx, ans_val = (0, 0), 0
        for i in range(len(array)):
            if array[i].isnumeric():
                count += 1
            else:
                count -= 1

            if count in dic:
                l, r = dic[count], i + 1
                if r - l + 1 > ans_val:
                    ans_idx, ans_val = (l, r), r - l + 1
            else:
                dic[count] = i + 1

            # print(i, count, ans_idx, ans_val, dic)

        return array[ans_idx[0]:ans_idx[1]]
```