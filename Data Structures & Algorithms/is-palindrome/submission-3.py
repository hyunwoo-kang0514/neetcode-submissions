class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        s2 = []

        cleaned = []

        for c in s:
            new_c = c.lower()
            if self.processInput(new_c):
                cleaned.append(new_c)

        half = len(cleaned) // 2

        for i, c in enumerate(cleaned):
            if i < half:
                s1.append(c)
            elif i >= len(cleaned) - half:
                s2.append(c)

        for i in range(len(s1)):
            e1 = s1.pop()
            e2 = s2.pop(0)

            if e1 != e2:
                return False

        return True

    def processInput(self, c):
        return ('a' <= c <= 'z') or ('0' <= c <= '9')