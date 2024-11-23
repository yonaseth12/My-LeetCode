class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        alice_wins = False
        for i in range(10, 0, -1):
            n -= i
            if n < 0: return alice_wins
            elif n == 0: return not alice_wins
            alice_wins = not alice_wins