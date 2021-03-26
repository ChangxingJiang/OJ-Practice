class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        lst = []
        for ch in S:
            if ch not in vowels:
                lst.append(ch)
        return "".join(lst)


if __name__ == "__main__":
    print(Solution().removeVowels("leetcodeisacommunityforcoders"))  # "ltcdscmmntyfrcdrs"
    print(Solution().removeVowels("aeiou"))  # ""
