class Solution:
    def maskPII(self, S: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().maskPII("LeetCode@LeetCode.com"))  # "l*****e@leetcode.com"
    print(Solution().maskPII("AB@qq.com"))  # "a*****b@qq.com"
    print(Solution().maskPII("1(234)567-890"))  # "***-***-7890"
    print(Solution().maskPII("86-(10)12345678"))  # "+**-***-***-5678"
