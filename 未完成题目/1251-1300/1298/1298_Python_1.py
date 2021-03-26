from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 16
    print(Solution().maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
                                containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]))

    # 6
    print(Solution().maxCandies(status=[1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1],
                                keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                                containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initialBoxes=[0]))

    # 1
    print(Solution().maxCandies(status=[1, 1, 1], candies=[100, 1, 100], keys=[[], [0, 2], []],
                                containedBoxes=[[], [], []], initialBoxes=[1]))

    # 0
    print(Solution().maxCandies(status=[1], candies=[100], keys=[[]], containedBoxes=[[]], initialBoxes=[]))

    # 7
    print(Solution().maxCandies(status=[1, 1, 1], candies=[2, 3, 2], keys=[[], [], []], containedBoxes=[[], [], []],
                                initialBoxes=[2, 1, 0]))
