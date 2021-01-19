class Solution:
    _CHANGE = {
        "2": 3,
        "4": 7,
        "5": 7,
        "6": 7,
        "8": 9,
    }

    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2

        while True:
            s = str(n)

            # 如果为偶数位，则必定为11或11的倍数
            if len(s) % 2 == 0 and n > 11:
                n = 10 ** len(s)

            # 如果开头为[2,4,5,6,8]，则末尾一定也是[2,4,5,6,8]，不可能为质数
            elif n > 10 and s[0] in self._CHANGE:
                n = self._CHANGE[s[0]] * (10 ** (len(s) - 1))

            # 判断是否为回文
            elif s != s[::-1]:
                n += 1

            else:
                # 判断是否为质数
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        n += 1
                        break
                else:
                    return n


if __name__ == "__main__":
    print(Solution().primePalindrome(6))  # 7
    print(Solution().primePalindrome(8))  # 11
    print(Solution().primePalindrome(13))  # 101
    print(Solution().primePalindrome(51115))  #
