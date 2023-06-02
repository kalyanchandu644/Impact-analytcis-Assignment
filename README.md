# Impact-analytcis-Assignment

Problem Statement:

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Approaches:
where # n: number of academic days # m: cannot miss m or more classes consecutively for our case m is 4
Recusive Approach:
Time Complexity: O( 2*n)
Space Complexity: O(n)
Basic Recursive approach
Memoization Approach:
Time Complexity: O(m * n)
Space Complexity: O(m * n)
Dynamic Programing Memoization
Tabulation Approach:
Time Complexity: O(m *n)
Space Complexity: O(m *n)
Tabulation with spoace optimised approach:
Time Complexity: O(m *n)
Space Complexity: O(m)

To run the file,

just run in commond prompt,
go to the main.py file path
python main.py
It will run for the inputs specified in the inputs array located in main.py
