class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """


if __name__ == "__main__":
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    obj.getHits(4)  # 3
    obj.hit(300)
    obj.getHits(300)  # 4
    obj.getHits(301)  # 3
