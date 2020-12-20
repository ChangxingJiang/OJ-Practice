from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().numOfBurgers(16, 7))  # [1,6]
    print(Solution().numOfBurgers(17, 4))  # []
    print(Solution().numOfBurgers(4, 17))  # []
    print(Solution().numOfBurgers(0, 0))  # [0,0]
    print(Solution().numOfBurgers(2, 1))  # [0,1]
