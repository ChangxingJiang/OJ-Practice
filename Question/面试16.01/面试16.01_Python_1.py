from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[1] ^ numbers[0]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers


if __name__ == "__main__":
    print(Solution().swapNumbers([1, 2]))  # [2,1]
