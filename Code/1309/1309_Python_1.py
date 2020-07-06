class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        idx = 0
        for i in range(len(s)):
            if i - idx > 2:
                ans += chr(int(s[idx]) + 96)
                idx += 1
            if s[i] == "#":
                ans += chr(int(s[idx:i]) + 96)
                idx = i + 1
        while idx < len(s):
            ans += chr(int(s[idx]) + 96)
            idx += 1
        return ans

        # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


if __name__ == "__main__":
    print(Solution().freqAlphabets("10#11#12"))  # jkab
    print(Solution().freqAlphabets("1326#"))  # acz
    print(Solution().freqAlphabets("25#"))  # y
    print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
    # abcdefghijklmnopqrstuvwxyz
