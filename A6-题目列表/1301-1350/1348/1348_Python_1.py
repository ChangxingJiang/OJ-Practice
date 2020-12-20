from typing import List


class TweetCounts:

    def __init__(self):
        pass

    def recordTweet(self, tweetName: str, time: int) -> None:
        pass

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        pass


# [et","getTweetCountsPerFrequency"]
# [["hour","tweet3",0,210]]

if __name__ == "__main__":
    obj = TweetCounts()
    obj.recordTweet("tweet3", 0)
    obj.recordTweet("tweet3", 60)
    obj.recordTweet("tweet3", 10)
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))  # [2]
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))  # [2,1]
    obj.recordTweet("tweet3", 120)
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 210))  # [4]
