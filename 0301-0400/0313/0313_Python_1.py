from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        size = len(primes)
        idx = [0] * size  # 当前查找坐标列表
        lst = [1]

        for i in range(n - 1):
            min_idx, min_val = [], float("inf")
            for j in range(size):
                val = lst[idx[j]] * primes[j]
                if val < min_val:
                    min_idx, min_val = [j], val
                elif val == min_val:
                    min_idx.append(j)

            for j in min_idx:
                idx[j] += 1
            lst.append(min_val)

        return lst[-1]


if __name__ == "__main__":
    # 32
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
