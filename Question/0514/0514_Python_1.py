class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        size = len(ring)

        def distance(a, b):
            if a > b:
                a, b = b, a
            return min(b - a, a + size - b)

        dp = [[-1] * len(ring) for _ in range(len(key) + 1)]

        dp[0][0] = 0

        for i in range(1, len(key) + 1):
            for j in range(size):
                if ring[j] == key[i - 1]:
                    # print(key[i - 1], j)
                    for k in range(size):
                        if dp[i - 1][k] != -1:
                            val = dp[i - 1][k] + distance(j, k) + 1
                            if dp[i][j] == -1 or dp[i][j] > val:
                                dp[i][j] = val

        # for dd in dp:
        #     print(dd)

        return min([v for v in dp[-1] if v != -1])


if __name__ == "__main__":
    print(Solution().findRotateSteps(ring="godding", key="gd"))  # 4
    print(Solution().findRotateSteps(ring="pqwcx", key="cpqwx"))  # 13
