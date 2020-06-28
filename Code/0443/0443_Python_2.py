from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        now = chars[-1]
        num = 1
        for i in range(len(chars) - 2, - 1, -1):
            if chars[i] == now:
                num += 1
                chars.pop(i + 1)
            else:
                if num > 1:
                    for j in str(num)[::-1]:
                        chars.insert(i + 2, j)
                now = chars[i]
                num = 1
        else:
            if num > 1:
                for j in str(num)[::-1]:
                    chars.insert(1, j)
        return len(chars)


if __name__ == "__main__":
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))  # 6
    print(Solution().compress(["a"]))  # 1
    print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # 4
