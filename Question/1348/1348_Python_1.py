import bisect
import collections
from typing import List


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


if __name__ == "__main__":
    obj = TweetCounts()
    obj.recordTweet("tweet3", 0)
    obj.recordTweet("tweet3", 60)
    obj.recordTweet("tweet3", 10)
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))  # [2]
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))  # [2,1]
    obj.recordTweet("tweet3", 120)
    print(obj.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))  # [4]
