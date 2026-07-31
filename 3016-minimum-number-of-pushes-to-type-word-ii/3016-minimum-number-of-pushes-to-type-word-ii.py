class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        from collections import Counter
        freq = sorted(Counter(word).values(), reverse=True)
        push = 0
        for i in range(len(freq)):
            push += freq[i] * (i // 8 + 1)
        return push