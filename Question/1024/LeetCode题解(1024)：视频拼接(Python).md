# LeetCode题解(1024)：拼接视频片段使覆盖整个时间段(Python)

题目：[原题链接](https://leetcode-cn.com/problems/video-stitching/)（中等）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 40ms (66%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()

        ans = 0
        last = 0
        now = 0

        for clip in clips:
            if last < clip[0]:
                if now >= clip[0]:
                    last = now
                    ans += 1
                else:
                    return -1

            if now < clip[1]:
                now = clip[1]

            if now >= T:
                return ans + 1

        return -1
```