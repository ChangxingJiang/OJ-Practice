import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = set()
        for email in emails:
            name, domain = email.split("@")
            total = re.sub("\+.*$", "", name.replace(".", "")) + "@" + domain
            if total not in hashmap:
                hashmap.add(total)
        return len(hashmap)


if __name__ == "__main__":
    print(Solution().numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
    # 2
