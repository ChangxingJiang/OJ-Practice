from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        pass


if __name__ == "__main__":
    print(Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))  # [true,true,true,false,true]
    print(Solution().kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))  # [true,false,false,false,false]
    print(Solution().kidsWithCandies(candies=[12, 1, 12], extraCandies=10))  # [true,false,true]
