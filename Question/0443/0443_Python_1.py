from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        now = None
        num = 0
        ans = ""
        for c in chars:
            if c == now:
                num += 1
            else:
                if now is not None:
                    if num > 1:
                        ans += now + str(num)
                    else:
                        ans += now
                now = c
                num = 1
        else:
            if num > 1:
                ans += now + str(num)
            else:
                ans += now
        chars.clear()
        chars.extend(list(ans))
        return len(ans)


if __name__ == "__main__":
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))  # 6
    print(Solution().compress(["a"]))  # 1
    print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # 4
