class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = [0] * 50
        for num in range(lowLimit, highLimit + 1):
            val = 0
            while num > 0:
                val += num % 10
                num //= 10
            count[val] += 1
        return max(count)


if __name__ == "__main__":
    print(Solution().countBalls(1, 10))  # 2
    print(Solution().countBalls(5, 15))  # 2
    print(Solution().countBalls(19, 28))  # 2
