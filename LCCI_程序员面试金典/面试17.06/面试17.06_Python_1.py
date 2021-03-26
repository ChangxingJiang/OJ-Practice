class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        ans = 0

        # 当前计算位
        now = 1
        while n > now:
            last1, last2 = 2 * now, 3 * now
            now *= 10
            a, b = divmod(n, now)

            ans += a * (last2 - last1)

            if last2 <= b:
                ans += last2 - last1
            elif last1 <= b < last2:
                ans += b - last1 + 1

        return ans


if __name__ == "__main__":
    print(Solution().numberOf2sInRange(25))  # 9
    print(Solution().numberOf2sInRange(100))  # 20
