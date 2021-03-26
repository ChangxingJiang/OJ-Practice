from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = set()
        for email in emails:
            idx = email.index("@")
            real = ""
            for n in email[:idx]:
                if n == "+":
                    break
                elif n != ".":
                    real += n
            real += email[idx:]
            if real not in hashmap:
                hashmap.add(real)
        return len(hashmap)


if __name__ == "__main__":
    print(Solution().numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
    # 2
