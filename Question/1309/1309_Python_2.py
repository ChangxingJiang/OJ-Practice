class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        queue = []
        for i in range(len(s)):
            if len(queue) > 2:
                ans += chr(int(queue.pop(0)) + 96)
            if s[i] == "#":
                ans += chr(int(queue.pop(0) + queue.pop(0)) + 96)
            else:
                queue.append(s[i])
        while queue:
            ans += chr(int(queue.pop(0)) + 96)
        return ans


if __name__ == "__main__":
    print(Solution().freqAlphabets("10#11#12"))  # jkab
    print(Solution().freqAlphabets("1326#"))  # acz
    print(Solution().freqAlphabets("25#"))  # y
    print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
    # abcdefghijklmnopqrstuvwxyz
