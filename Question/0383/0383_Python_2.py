class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = [0] * 26

        # 遍历统计杂志中个字母的数量
        for c in magazine:
            hashmap[ord(c) - 97] += 1

        # 遍历赎金信判断杂志中字母数量是否充足
        for c in ransomNote:
            if hashmap[ord(c) - 97] <= 0:
                return False
            else:
                hashmap[ord(c) - 97] -= 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().canConstruct("a", "b"))  # False
    print(Solution().canConstruct("aa", "ab"))  # False
    print(Solution().canConstruct("aa", "aab"))  # True
