class Solution:
    def maskPII(self, S: str) -> str:
        # 处理电子邮箱的情况
        if "@" in S:
            i = S.index("@")
            S = S.lower()
            return S[0] + "*****" + S[i - 1:]

        # 处理电话的情况
        else:
            def is_digit(ch):
                return ch.isdigit()

            S = "".join(list(filter(is_digit, S)))
            if len(S) == 10:
                return "***-***-" + S[-4:]
            else:
                return "+" + "*" * (len(S) - 10) + "-***-***-" + S[-4:]


if __name__ == "__main__":
    print(Solution().maskPII("LeetCode@LeetCode.com"))  # "l*****e@leetcode.com"
    print(Solution().maskPII("AB@qq.com"))  # "a*****b@qq.com"
    print(Solution().maskPII("1(234)567-890"))  # "***-***-7890"
    print(Solution().maskPII("86-(10)12345678"))  # "+**-***-***-5678"
    print(Solution().maskPII("+86(88)1513-7-74"))  # "+*-***-***-3774"
