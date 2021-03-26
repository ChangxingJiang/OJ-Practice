class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num) // 2 + 1):  # 长度可能接近一半：1991+1=1992
            for j in range(i + 1, i + (len(num) - i) // 2 + 1):
                v1, v2 = int(num[:i]), int(num[i:j])
                # 不能为0开头
                if v1 != 0 and num[0] == "0":
                    continue
                if v2 != 0 and num[i] == "0":
                    continue

                k = j
                while k <= len(num):
                    if k == len(num):
                        return True
                    v3 = v1 + v2
                    s3 = str(v3)
                    if num[k:k + len(s3)] == s3:
                        v1, v2 = v2, v3
                        k += len(s3)
                    else:
                        break
        return False


if __name__ == "__main__":
    print(Solution().isAdditiveNumber("112358"))  # True
    print(Solution().isAdditiveNumber("199100199"))  # True
    print(Solution().isAdditiveNumber("199111992"))  # False
    print(Solution().isAdditiveNumber("0235813"))  # False
