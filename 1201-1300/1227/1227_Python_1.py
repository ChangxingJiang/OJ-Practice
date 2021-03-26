class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n > 1 else 1


if __name__ == "__main__":
    print(Solution().nthPersonGetsNthSeat(1))  # 1
    print(Solution().nthPersonGetsNthSeat(2))  # 0.5
