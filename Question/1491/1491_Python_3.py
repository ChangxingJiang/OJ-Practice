from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        size = len(salary)

        total = 0
        min_val, max_val = 10 ** 6, 10 ** 3

        for n in salary:
            total += n
            if n < min_val:
                min_val = n
            if n > max_val:
                max_val = n

        return (total - min_val - max_val) / (size - 2)


if __name__ == "__main__":
    print(Solution().average(salary=[4000, 3000, 1000, 2000]))  # 2500
    print(Solution().average(salary=[1000, 2000, 3000]))  # 2000
    print(Solution().average(salary=[6000, 5000, 4000, 3000, 2000, 1000]))  # 3500
    print(Solution().average(salary=[8000, 9000, 2000, 3000, 6000, 1000]))  # 4750
