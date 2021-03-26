from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        size = len(word)
        for i in range(2 ** size):
            pattern = bin(i)[2:].zfill(size)
            res = []
            for j in range(size):
                if pattern[j] == "0":
                    res.append(word[j])
                else:
                    if res and res[-1].isnumeric():
                        res[-1] = str(int(res[-1]) + 1)
                    else:
                        res.append("1")
            ans.append("".join(res))

        return ans


if __name__ == "__main__":
    # ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
    print(Solution().generateAbbreviations("word"))
