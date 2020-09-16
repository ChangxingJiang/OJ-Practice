class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return (ans * n) % 1000000007


if __name__ == "__main__":
    print(Solution().cuttingRope(2))  # 1
    print(Solution().cuttingRope(10))  # 36
