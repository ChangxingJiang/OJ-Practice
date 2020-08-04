from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().asteroidCollision(asteroids=[5, 10, -5]))  # [5, 10]
    print(Solution().asteroidCollision(asteroids=[8, -8]))  # []
    print(Solution().asteroidCollision(asteroids=[10, 2, -5]))  # [10]
