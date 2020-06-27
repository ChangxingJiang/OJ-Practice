def guess(num: int) -> int:
    if num < 6:
        return -1
    elif num == 6:
        return 0
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().guessNumber(10))  # 6
