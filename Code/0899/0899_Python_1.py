class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            now = S
            for i in range(len(S)):
                tmp = S[i:] + S[:i]
                if tmp < now:
                    now = tmp
            return now
        else:
            return "".join(sorted(list(S)))


if __name__ == "__main__":
    print(Solution().orderlyQueue(S="cba", K=1))  # "acb"
    print(Solution().orderlyQueue(S="baaca", K=3))  # "aaabc"
