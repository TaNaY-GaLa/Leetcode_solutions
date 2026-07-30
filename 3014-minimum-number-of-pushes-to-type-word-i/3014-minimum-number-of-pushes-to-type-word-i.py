class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        push = 0
        for i in range(len(word)):
            push =push+ (i // 8) + 1
        return push