from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # 字符转换
        def shift(ch, n):
            return chr((ord(ch) - 97 + n) % 26 + 97)

        # 反向遍历字符串
        ans = []
        now = 0
        for i in range(len(shifts) - 1, -1, -1):
            now += shifts[i]
            ans.append(shift(S[i], now))

        # 反转生成结果
        return "".join(reversed(ans))


if __name__ == "__main__":
    print(Solution().shiftingLetters(S="abc", shifts=[3, 5, 9]))  # "rpl"
