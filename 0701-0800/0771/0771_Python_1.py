class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for j in J:
            ans += S.count(j)
        return ans


if __name__ == "__main__":
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))  # 3
    print(Solution().numJewelsInStones("z", "ZZ"))  # 0
