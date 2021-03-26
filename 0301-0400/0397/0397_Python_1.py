class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            # 处理n为偶数的情况
            if n % 2 == 0:
                n //= 2
            else:
                # 处理特殊的奇数3
                if n == 3:
                    n -= 1
                else:
                    if n % 4 == 1:
                        n -= 1
                    else:
                        n += 1
            ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().integerReplacement(8))  # 3
    print(Solution().integerReplacement(7))  # 4
    print(Solution().integerReplacement(4))  # 2
