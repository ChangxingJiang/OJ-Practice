# LeetCode题解(1542)：找出最长的可通过字符交换转变为回文串的子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-longest-awesome-substring/)（困难）

标签：字符串、哈希表、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1908ms (35.27%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 320ms (97.10%)  |
| Ans 3 (Python) |            |            |                 |

解法一（哈希表）：

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 0
        now = 0  # 当前各个数字的奇偶状态
        hashmap = {now: 0}  # 每个奇偶状态的最早出现坐标
        for i, ch in enumerate(s):
            # 计算当前数字添加后奇偶状态的变化
            now ^= 1 << int(ch)
            if now not in hashmap:
                hashmap[now] = i + 1

            # 计算当前奇偶状态构成回文串的最早坐标
            if now in hashmap:
                ans = max(ans, i - hashmap[now] + 1)
            for j in range(10):
                tmp = now ^ (1 << j)
                if tmp in hashmap:
                    ans = max(ans, i - hashmap[tmp] + 1)
            # print(i, "[", ch, "]", bin(now)[2:], "->", ans)

        return ans
```

解法二（优化解法一）：

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        status = 0  # 当前各个数字的奇偶状态
        hashmap = {status: [0, 0]}  # 每个奇偶状态的最早出现坐标
        for i, ch in enumerate(s):
            # 计算当前数字添加后奇偶状态的变化
            status ^= 1 << int(ch)
            if status not in hashmap:
                hashmap[status] = [i + 1, i + 1]
            else:
                hashmap[status][1] = i + 1

        # 计算当前奇偶状态构成回文串的最早坐标
        ans = 1
        for status in hashmap:
            ans = max(ans, hashmap[status][1] - hashmap[status][0])
            for j in range(10):
                if (tmp := status ^ (1 << j)) in hashmap:
                    ans = max(ans, hashmap[status][1] - hashmap[tmp][0])

        return ans
```





