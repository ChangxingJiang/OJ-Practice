# LeetCode题解(1156)：移动一个字符形成的单字符重复子串的最大长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 108ms (31.37%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 76ms (75.49%)  |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符出现的频次
        count = collections.Counter(text)

        # 统计最长子串
        ans = 0
        queue = []
        for ch in text:
            need_remove = []
            find = False
            for i in range(len(queue)):
                elem = queue[i]
                if ch == elem[0]:
                    elem[1] += 1
                    if not elem[2]:
                        find = True
                else:
                    if elem[2]:
                        if elem[1] < count[elem[0]]:
                            elem[1] += 1
                        ans = max(ans, elem[1])
                        need_remove.append(i)
                    else:
                        elem[2] = True
            for i in need_remove[::-1]:
                queue.pop(i)
            if not find:
                queue.append([ch, 1, False])
        for elem in queue:
            if elem[1] < count[elem[0]]:
                elem[1] += 1
            ans = max(ans, elem[1])
        return ans
```

解法二（两次遍历，以块作为队列单位）：

```python
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符出现的频次
        count = collections.Counter(text)

        # 将队列整理成块
        queue = []
        for ch in text:
            if not queue or ch != queue[-1][0]:
                queue.append([ch, 1])
            else:
                queue[-1][1] += 1

        ans = 0

        # 计算最长子串
        for i in range(len(queue)):
            elem = queue[i]
            length = elem[1]
            if i + 2 < len(queue):
                if queue[i + 1][1] == 1 and elem[0] == queue[i + 2][0]:
                    length += queue[i + 2][1]
            if length < count[elem[0]]:
                length += 1
            ans = max(ans, length)

        return ans
```





