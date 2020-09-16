class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))  # holle
    print(Solution().reverseVowels("leetcode"))  # leotcede
    print(Solution().reverseVowels("aA"))  # Aa
