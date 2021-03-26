class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lst = set()
        for ch in s:
            if ch not in lst:
                lst.add(ch)
            else:
                lst.remove(ch)
        return len(lst) <= 1


if __name__ == "__main__":
    print(Solution().canPermutePalindrome("tactcoa"))  # True
