class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        size = len(a)

        # 第1种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if a[left] != b[right]:
                    if b[left] == b[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if b[left] != b[right]:
                    right = False
                    break
        if right:
            print("第1种拼接")
            return True

        # 第2种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if a[left] != b[right]:
                    if a[left] == a[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if a[left] != a[right]:
                    right = False
                    break
        if right:
            print("第2种拼接")
            return True

        # 第3种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if b[left] != a[right]:
                    if a[left] == a[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if a[left] != a[right]:
                    right = False
                    break
        if right:
            print("第3种拼接")
            return True

        # 第4种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if b[left] != a[right]:
                    if b[left] == b[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if b[left] != b[right]:
                    right = False
                    break
        if right:
            print("第4种拼接")
            return True

        return False


if __name__ == "__main__":
    print(Solution().checkPalindromeFormation(a="x", b="y"))  # True
    print(Solution().checkPalindromeFormation(a="abdef", b="fecab"))  # False
    print(Solution().checkPalindromeFormation(a="ulacfd", b="jizalu"))  # True
    print(Solution().checkPalindromeFormation(a="aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", b="uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))  # True
