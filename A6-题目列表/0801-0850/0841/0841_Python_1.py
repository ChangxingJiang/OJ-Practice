from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))  # True
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # False
