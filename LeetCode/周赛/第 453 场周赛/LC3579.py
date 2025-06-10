from collections import Counter


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        dp = [n + 2] * (n + 1)
        dp[0] = 0  # 上一刀落在哪儿
        for i in range(1, n + 1):
            for j in range(0, i):  # 上一刀落在哪儿
                res = dp[j] + self.cal_all(word1[j:i], word2[j:i])
                # print(f"i={i}, j={j}: dp[{j}]={dp[j]}, value={self.cal_all(word1, word2, j, i)}")
                dp[i] = min(dp[i], res)
        # print(dp)
        return dp[- 1]

    @staticmethod
    def cal_all(word1: str, word2: str) -> int:
        """计算字符串 s 不切分的最优解"""
        return min(Solution.cal_only_1_2(word1, word2),
                   Solution.cal_only_1_2(word1[::-1], word2) + 1)

    @staticmethod
    def cal_only_1_2(word1: str, word2: str) -> int:
        change = Counter()
        res = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                res += 1
                if change[(word2[i], word1[i])] >= 1:
                    change[(word2[i], word1[i])] -= 1
                    res -= 1
                else:
                    change[(word1[i], word2[i])] += 1

        return res

    @staticmethod
    def cal_only_1(word1: str, word2: str, i1: int, i2: int) -> int:
        """只执行替换操作的操作数"""
        res = 0
        for i in range(i1, i2):
            if word1[i] != word2[i]:
                res += 1
        return res


if __name__ == "__main__":
    print(Solution().minOperations("abcdf", "dacbe"))  # 4
    print(Solution().minOperations("abceded", "baecfef"))  # 4
    print(Solution().minOperations("abcdef", "fedabc"))  # 2

    # 536 / 637
    print(Solution().minOperations("abcebc", "ecbade"))  # 3

    # 633 / 637
    print(Solution().minOperations("bcbeacabdbceeebda", "bddbcceadbebaabee"))  # 8

    print("其他自测: ")
    print(Solution.cal_only_1_2("ab", "da"))  # 2
    print(Solution.cal_only_1_2("ded", "fef"))  # 2
    print(Solution.cal_only_1_2("ab", "ba"))  # 1
    print(Solution.cal_all("abcdef", "fedabc"))  # 2
    print(Solution.cal_all("abcd", "dacb"))  # 3
    print(Solution.cal_only_1_2("abcd", "dacb"))  # 3
    print(Solution.cal_only_1_2("dcba", "dacb"))  # 3
    print(Solution.cal_only_1_2("aacc", "ccaa"))  # 2
