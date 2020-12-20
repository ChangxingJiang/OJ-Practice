from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        pass


if __name__ == "__main__":
    # [3,1,5]
    print(Solution().filterRestaurants(
        restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
        veganFriendly=1, maxPrice=50, maxDistance=10))

    # [4,3,2,1,5]
    print(Solution().filterRestaurants(
        restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
        veganFriendly=0, maxPrice=50, maxDistance=10))

    # [4,5]
    print(Solution().filterRestaurants(
        restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
        veganFriendly=0, maxPrice=30, maxDistance=3))
