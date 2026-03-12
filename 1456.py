class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        cur = max_vowels = len([l for l in s[:k] if l in vowels])

        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i-k] in vowels:
                cur -= 1
            if cur > max_vowels:
                max_vowels = cur

        return max_vowels
        