from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = n // 2
        if n % 2 == 0:
            return [i for i in range(-m, 0)] + [i for i in range(1, m + 1)]
        else:
            return [i for i in range(-m, m + 1)]


if __name__ == "__main__":
    print(Solution().sumZero(5))  # [-7,-1,1,3,4]
    print(Solution().sumZero(3))  # [-1,0,1]
    print(Solution().sumZero(4))  # [-1,0,1]
    print(Solution().sumZero(1))  # [0]
