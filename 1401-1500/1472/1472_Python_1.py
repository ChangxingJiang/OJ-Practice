import collections


class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.size = 1
        self.array = collections.deque([homepage])

    def visit(self, url: str) -> None:
        self.i += 1
        if self.i == len(self.array):
            self.array.append(url)
        else:
            self.array[self.i] = url
        self.size = self.i + 1

    def back(self, steps: int) -> str:
        self.i -= steps
        if self.i < 0:
            self.i = 0
        return self.array[self.i]

    def forward(self, steps: int) -> str:
        self.i += steps
        if self.i >= self.size:
            self.i = self.size - 1
        return self.array[self.i]


if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    print(browserHistory.back(1))  # "facebook.com"
    print(browserHistory.back(1))  # "google.com"
    print(browserHistory.forward(1))  # "facebook.com"
    browserHistory.visit("linkedin.com")
    print(browserHistory.forward(2))  # "linkedin.com"
    print(browserHistory.back(2))  # "google.com"
    print(browserHistory.back(7))  # "leetcode.com"

    print()

    browserHistory = BrowserHistory("esgriv.com")
    browserHistory.visit("cgrt.com")
    browserHistory.visit("tip.com")
    print(browserHistory.back(9))  # "esgriv.com"
    browserHistory.visit("kttzxgh.com")
    print(browserHistory.forward(7))  # "kttzxgh.com"
    browserHistory.visit("crqje.com")
    browserHistory.visit("iybch.com")
    print(browserHistory.forward(5))  # "iybch.com"

