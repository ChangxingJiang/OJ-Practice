class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        distance = 0
        while n:
            if n & 1 == 1:
                distance += 1
            n = n >> 1
        return distance


if __name__ == "__main__":
    print(Solution().hammingDistance(1, 4))  # 2
