import collections


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N1 = len(s)
        N2 = len(t)

        # 处理字符串s比字符串t短的情况
        if N1 < N2:
            return 0

        # 生成字符串中各个字符的坐标位置字典
        count = collections.defaultdict(list)
        for i, c in enumerate(t):
            count[c].append(i)

        stats = [1] + [0] * N2  # 当前行状态

        for ch in s:  # 遍历字符串s
            for j in count[ch][::-1]:  # 如果当前字符存在于j中，则遍历当前字符在j中的所有坐标
                stats[j + 1] += stats[j]  # 则累加当前位置的状态数

        return stats[-1]


if __name__ == "__main__":
    print(Solution().numDistinct(s="rabbbit", t="rabbit"))  # 3
    print(Solution().numDistinct(s="babgbag", t="bag"))  # 5
