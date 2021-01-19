import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p //= g
        q //= g

        if p % 2 == 1 and q % 2 == 1:
            return 1

        if p % 2 == 0 and q % 2 == 1:
            return 2

        return 0


if __name__ == "__main__":
    print(Solution().mirrorReflection(2, 1))  # 2
