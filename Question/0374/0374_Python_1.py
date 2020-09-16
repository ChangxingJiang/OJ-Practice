def guess(num: int) -> int:
    if num > 6:
        return -1
    elif num == 6:
        return 0
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        s = 0
        while True:
            m = (s + n) // 2
            ans = guess(m)
            if ans == -1:
                n = m - 1
            elif ans == 1:
                s = m + 1
            else:
                return m


if __name__ == "__main__":
    print(Solution().guessNumber(10))  # 6
