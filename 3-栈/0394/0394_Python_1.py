class Solution:
    def decodeString(self, s: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(Solution().decodeString("3[a2[c]]"))  # "accaccacc"
    print(Solution().decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(Solution().decodeString("abc3[cd]xyz"))  # "abccdcdcdxyz"
