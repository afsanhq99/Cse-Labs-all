def getLCS(a, b):
    dp = []
    for i in range(len(a) + 1):
        row = []
        for j in range(len(b) + 1):
            row.append(0)
        dp.append(row)

    # fill dp with values using following logic
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # atlast return dp[len(a)][len(b)] which is the longest LCS value of a and b
    return dp[len(a)][len(b)]


# method that returns LCS of all the strings present in list
def LCS(lst):
    # initialise minLen to some maximum value
    minLen = 9999999999

    # loop the lst value by value
    for i in range(1, len(lst), 1):
        # get LCS len between lst[0] and lst[i]
        lcsLen = getLCS(lst[0], lst[i])
        # update minLen value
        minLen = min([minLen, lcsLen])

    # atlast return minLen which is the LCS value of all strings in list
    return minLen


# testing main method
def main():
    print(LCS(['hell', 'hello', 'bella']))  # prints "3"
    print(LCS(['abbcdab', 'daccbadb', 'abccdaab']))  # prints "4"


main()