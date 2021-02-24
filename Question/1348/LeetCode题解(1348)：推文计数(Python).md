# LeetCode题解(1348)：推文计数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/tweet-counts-per-frequency/)（中等）

标签：设计、有序映射

| 解法           | 时间复杂度                                                  | 空间复杂度 | 执行用时       |
| -------------- | ----------------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | recordTweet = $O(1)$ ; getTweetCountsFrequency = $O(NlogN)$ | $O(N)$     | 208ms (89.47%) |
| Ans 2 (Python) |                                                             |            |                |
| Ans 3 (Python) |                                                             |            |                |

解法一：

```python
class TweetCounts:
    _FREQUENTY = {
        "day": 3600 * 24,
        "hour": 3600,
        "minute": 60
    }

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        self.tweets[tweetName].sort()
        lst = self.tweets[tweetName]
        idx = bisect.bisect_left(lst, startTime)

        ans = []
        for start in range(startTime, endTime + 1, self._FREQUENTY[freq]):
            end = min(start + self._FREQUENTY[freq], endTime + 1)
            res = 0
            while idx < len(lst) and lst[idx] < end:
                res += 1
                idx += 1
            ans.append(res)

        return ans
```

