import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)

        ans = [0] * 10
        ans[0] = count["z"]
        ans[2] = count["w"]
        ans[4] = count["u"]
        ans[6] = count["x"]
        ans[8] = count["g"]
        ans[5] = count["f"] - ans[4]
        ans[3] = count["h"] - ans[8]
        ans[7] = count["s"] - ans[6]
        ans[9] = count["i"] - ans[5] - ans[6] - ans[8]
        ans[1] = count["n"] - ans[7] - 2 * ans[9]

        return "".join(str(i) * n for i, n in enumerate(ans))


if __name__ == "__main__":
    print(Solution().originalDigits("owoztneoer"))  # "012"
    print(Solution().originalDigits("fviefuro"))  # "45"
