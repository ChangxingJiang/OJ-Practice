class Solution:
    def reformat(self, s: str) -> str:
        alphas = []
        nums = []
        for c in s:
            if c.isalpha():
                alphas.append(c)
            else:
                nums.append(c)

        if abs(len(alphas) - len(nums)) > 1:
            return ""

        ans = ""
        if len(alphas) < len(nums):
            for i in range(len(alphas)):
                ans += nums[i] + alphas[i]
            else:
                ans += nums[-1]
            return ans
        elif len(alphas) > len(nums):
            for i in range(len(nums)):
                ans += alphas[i] + nums[i]
            else:
                ans += alphas[-1]
        else:
            for i in range(len(nums)):
                ans += alphas[i] + nums[i]

        return ans


if __name__ == "__main__":
    print(Solution().reformat(s="a0b1c2"))  # "0a1b2c"
    print(Solution().reformat(s="leetcode"))  # ""
    print(Solution().reformat(s="1229857369"))  # ""
    print(Solution().reformat(s="covid2019"))  # "c2o0v1i9d"
    print(Solution().reformat(s="ab123"))  # "1a2b3"
