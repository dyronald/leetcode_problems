class Solution:
    def reverse_words(self, s: str) -> str:
        result = ''
        while True:
            last_space = s.rfind(' ')
            if last_space == -1:
                break

            result += ' ' + s[last_space+1:]
            s = s[:last_space].strip()

        result += ' ' + s
        return result.strip()
