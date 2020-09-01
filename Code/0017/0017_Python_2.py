from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]}

        def backtrack(now, next_digits):
            if not next_digits:
                ans.append(now)
            else:
                for d in phone[next_digits[0]]:
                    backtrack(now + d, next_digits[1:])

        ans = []
        if digits:
            backtrack("", digits)
        return ans


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(Solution().letterCombinations(""))  # []
