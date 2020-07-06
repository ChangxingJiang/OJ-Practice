class Solution:
    def reformat(self, s: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().reformat(s="a0b1c2"))  # "0a1b2c"
    print(Solution().reformat(s="leetcode"))  # ""
    print(Solution().reformat(s="1229857369"))  # ""
    print(Solution().reformat(s="covid2019"))  # "c2o0v1i9d"
    print(Solution().reformat(s="ab123"))  # "1a2b3"
