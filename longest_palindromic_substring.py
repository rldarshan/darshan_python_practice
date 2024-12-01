def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    # Initialize a table to store results
    dp = [[False] * n for _ in range(n)]

    # Every single character is a palindrome
    max_length = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    # Check for palindromic substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Check if the substring is palindromic
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

    # Return the longest palindromic substring
    return s[start:start + max_length]

# Example usage
s = "mylevelisveryhighinmalayalamlanguage"
print(longest_palindromic_substring(s))
