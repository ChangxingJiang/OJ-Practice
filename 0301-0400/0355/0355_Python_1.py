import collections
from typing import List


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
                self._follow[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # [6,5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # [5]
    print()

    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(1, 13)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(1, 505)
    twitter.postTweet(1, 333)
    twitter.postTweet(1, 22)
    twitter.postTweet(1, 11)
    print(twitter.getNewsFeed(1))  # [11,22,333,505,94,2,10,13,101,3]
