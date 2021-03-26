class Solution:
    def firstUniqChar(self, s: str) -> str:
        order = []
        more = set()
        maybe = set()
        for ch in s:
            if ch not in more:
                if ch in maybe:
                    maybe.remove(ch)
                    more.add(ch)
                else:
                    order.append(ch)
                    maybe.add(ch)

        ans = sorted(maybe, key=lambda x: order.index(x))

        return ans[0] if ans else " "


if __name__ == "__main__":
    print(Solution().firstUniqChar("abaccdeff"))  # "b"
    print(Solution().firstUniqChar(""))  # " "
    print(Solution().firstUniqChar("leetcode"))  # "l"
