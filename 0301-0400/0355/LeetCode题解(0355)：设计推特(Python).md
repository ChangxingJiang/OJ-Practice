# LeetCode题解(0355)：设计推特(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-twitter/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 92ms (98.35%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Twitter:

    def __init__(self):
        self._now = 0  # 当前时间
        self._tweet = collections.defaultdict(collections.deque)  # 用户推文
        self._follow = collections.defaultdict(set)  # 用户关注

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 一旦发布推文，则默认自己关注自己
        if not self._tweet[userId]:
            self._follow[userId].add(userId)

        # 发布推文并推动时间更新
        self._tweet[userId].append((tweetId, self._now))
        self._now += 1

        # 控制推文存储总数，移除过早的推文
        if len(self._tweet[userId]) > 10:
            self._tweet[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for followee in self._follow[userId]:
            tweets.extend(self._tweet[followee])
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # 自己不能取关自己
            if followeeId in self._follow[followerId]:
                self._follow[followerId]._remove(followeeId)
```