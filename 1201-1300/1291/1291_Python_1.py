from typing import List

nums = []
for i in range(2, 10):
    v1 = int("".join([str(j) for j in range(1, i + 1)]))
    v2 = int("1" * i)
    nums.append(v1)
    for _ in range(9 - i):
        v1 += v2
        nums.append(v1)


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [num for num in nums if low <= num <= high]


if __name__ == "__main__":
    # [123,234]
    print(Solution().sequentialDigits(low=100, high=300))

    # [1234,2345,3456,4567,5678,6789,12345]
    print(Solution().sequentialDigits(low=1000, high=13000))
