from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


class GraduationCeremony:
    def __init__(self, n, m):
        # n: number of academic days
        # m: cannot miss m or more classes consecutively
        if n < m or n < 0 or m < 0:
            raise Exception("Invalid Inputs")

        self.n = n
        self.m = m
    

    def recursive_approach(self):
        """
        Time Complexity: O( 2*n)
        Space Complexity: O(n)
        Basic Recursive approach
        """
        def rec(n, m):
            if self.m == m:
                return 0
            if n == 0:
                return 1

            return rec(n - 1, 0) + rec(n - 1, m + 1)

        x1 = rec(self.n, 0)  # total number of valid ways to attend classes
        x2 = rec(self.n - 1, 1)  # total number of ways to miss the last day

        return f"{x2}/{x1}"

    def memoization_approach(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        Dynamic Programing Memoization
        """

        @lru_cache(None)
        def rec(n, m):

            if self.m == m:
                return 0
            if n == 0:
                return 1

            return rec(n - 1, 0) + rec(n - 1, m + 1)

        x1 = rec(self.n, 0)  # total number of valid way to attend classes
        x2 = rec(self.n - 1, 1)  # total number of way to miss last day

        return f"{x2}/{x1}"

    def tabulation_approach(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        Dynamic Programing Tabulation
        """

        n, m = self.n, self.m
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(m):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        x1 = dp[n][0]  # total number of valid way to attend classes
        x2 = dp[n - 1][1]  # total number of way to miss last day

        return f"{x2}/{x1}"

    def space_optimization_approach(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        Dynamic Programing Tabulation with Space Optimization
        """

        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # total number of valid way to attend classes
        x2 = temp[1]  # total number of way to miss last day

        return f"{x2}/{x1}"
    
    

    def run(self):
        print("For input" +" "+str(self.n)+ " "+"days")
        print()
        print('Recursive approach', self.recursive_approach())
        print()
        print('Memoization_approach1:', self.memoization_approach())
        print()
        print('Tabulation approach:', self.tabulation_approach())
        print()
        print('Space Optimized approach', self.space_optimization_approach())
        print('*' * 20,)
        print()

