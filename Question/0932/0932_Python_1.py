from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N <= 2:
            return [i for i in range(1, N + 1)]
        else:
            d, r = divmod(N, 2)
            a, b = d + r, d
            res1 = self.beautifulArray(a)
            res2 = self.beautifulArray(b)
            res1 = [n * 2 - 1 for n in res1]
            res2 = [n * 2 for n in res2]
            return res1 + res2


if __name__ == "__main__":
    print(Solution().beautifulArray(4))  # [2,1,4,3]
    print(Solution().beautifulArray(5))  # [3,1,2,5,4]
    print(Solution().beautifulArray(8))  # [1,5,3,7,2,6,4,8]
