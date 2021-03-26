class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = set()
        for ch in s:
            if ch not in count:
                count.add(ch)
            else:
                count.remove(ch)
        return len(count) <= 1


if __name__ == "__main__":
    print(Solution().canPermutePalindrome("code"))  # False
    print(Solution().canPermutePalindrome("aab"))  # True
    print(Solution().canPermutePalindrome("carerac"))  # True
