class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        distance = 0
        while n:
            distance += 1
            n = n & (n - 1)
        return distance


if __name__ == "__main__":
    print(Solution().hammingDistance(1, 4))  # 2
