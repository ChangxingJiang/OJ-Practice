from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if 2 * cheeseSlices <= tomatoSlices <= 4 * cheeseSlices and tomatoSlices % 2 == 0:
            n1 = (tomatoSlices - 2 * cheeseSlices) // 2
            n2 = cheeseSlices - n1
            return [n1, n2]
        else:
            return []


if __name__ == "__main__":
    print(Solution().numOfBurgers(16, 7))  # [1,6]
    print(Solution().numOfBurgers(17, 4))  # []
    print(Solution().numOfBurgers(4, 17))  # []
    print(Solution().numOfBurgers(0, 0))  # [0,0]
    print(Solution().numOfBurgers(2, 1))  # [0,1]
