from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxEvents(events=[[1, 2], [2, 3], [3, 4]]))  # 3
    print(Solution().maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))  # 4
    print(Solution().maxEvents(events=[[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))  # 4
    print(Solution().maxEvents(events=[[1, 100000]]))  # 1
    print(Solution().maxEvents(events=[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]))  # 7
