class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(ch) for ch in str(num)]
        for i in range(len(num)):
            max_idx, mav_val = i, num[i]
            for j in range(i + 1, len(num)):
                if mav_val <= num[j] and num[i] < num[j]:
                    max_idx, mav_val = j, num[j]
            if max_idx != i:
                num[i], num[max_idx] = num[max_idx], num[i]
                break
        return int("".join(str(i) for i in num))


if __name__ == "__main__":
    print(Solution().maximumSwap(2736))  # 7236
    print(Solution().maximumSwap(9973))  # 9973
    print(Solution().maximumSwap(1993))  # 9913
    print(Solution().maximumSwap(98368))  # 98863
