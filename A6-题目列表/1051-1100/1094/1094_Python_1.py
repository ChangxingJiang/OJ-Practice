from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))  # False
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))  # True
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))  # True
    print(Solution().carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))  # True
