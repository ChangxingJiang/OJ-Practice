from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for weight in asteroids:
            if weight > 0:
                stack.append(weight)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] < -weight:
                        stack.pop()
                    elif stack[-1] == -weight:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(weight)
        return stack


if __name__ == "__main__":
    print(Solution().asteroidCollision(asteroids=[5, 10, -5]))  # [5, 10]
    print(Solution().asteroidCollision(asteroids=[8, -8]))  # []
    print(Solution().asteroidCollision(asteroids=[10, 2, -5]))  # [10]
