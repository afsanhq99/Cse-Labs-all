

odd = 0
even = 0
noParity = 0
palindrome = 0
nonPalindrome = 0

def palindrome_check(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def readFile():
    input_file = open("LAb1input.txt", "r")
    inputs = []
    for line in input_file:
        inputs.append(line.split())
        try:
            inputs[-1][0] = int(inputs[-1][0])
        except:
            inputs[-1][0] = float(inputs[-1][0])
    input_file.close()
    return inputs


def writeOutput(inputs):
    global odd, even, noParity, palindrome, nonPalindrome

    OutputFile = open("output.txt", "w")
    for input in inputs:
        num, s = input[0], input[1]
        output =""
        if isinstance(num,int):
            if num % 2 == 0:
                even += 1
                output += f"{num} has even parity "
            else:
                odd += 1
                output +=f"{num} has odd parity "
        else:
            noParity += 1
            output += f"{num} cannot have parity "

        if palindrome_check(s):
            palindrome += 1
            output += f"and {s} is a palindrome\n"
        else:
            nonPalindrome += 1
            output += f"and {s} is not a palindrome\n"
        OutputFile.writelines(output)
    OutputFile.close()


# Writes percentages to record.txt file
def writeRecord():
    recordFile = open("record.txt", "w")
    recordFile.writelines(f"Percentage of odd parity: {((odd / (odd + even + noParity)) * 100)}%\n")
    recordFile.writelines(f"Percentage of even parity: {((even / (odd + even + noParity)) * 100)}%\n")
    recordFile.writelines(f"Percentage of no parity: {((noParity / (odd + even + noParity)) * 100)}%\n")
    recordFile.writelines(f"Percentage of palindrome: {(palindrome / (palindrome + nonPalindrome)) * 100}%\n")
    recordFile.writelines(f"Percentage of palindrome: {(nonPalindrome / (palindrome + nonPalindrome)) * 100}%\n")
    recordFile.close()




inputs = readFile()
writeOutput(inputs)
writeRecord()