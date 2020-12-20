from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[5],[0,1,2],[3,4,6]]
    print(Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))

    # [[1],[0,5],[2,3,4]]
    print(Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
