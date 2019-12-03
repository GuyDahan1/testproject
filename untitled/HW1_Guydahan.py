import math

# assignment1
"""func get a number in string and return intger"""


def parseStr(strNum, neg=0):
    num = 0
    revCounter = len(strNum) - 1
    if strNum[0] == '-':
        num = parseStr(strNum[1:], 1)
        return num
    for i in range(len(strNum)):
        temp = ord(strNum[revCounter]) - 48
        temp = temp * 10 ** i
        num = num + temp
        revCounter -= 1
    if neg == 1:
        return 0 - num
    return num

print(parseStr('1000'))
print(parseStr('15'))
print(parseStr('0'))
print(parseStr('-10'))

# assignment2
"""func get list and if its legal , func return hash"""


def smallHash(list):
    prev = list[0]
    if len(list) == 1 and 0 <= list[0] < 256:
        return list[0]
    if len(list) == 1 and 0 > list[0] or list[0] > 255:
        return "invalid value"
    for i in range(1, len(list)):
        if list[i] < 0 or list[i] > 256:
            return "invalid value"
        current = ((31 * prev) ^ list[i]) & 0xFF
        prev = current
    return current


print(smallHash([5]))
print(smallHash([5,6]))
print(smallHash([5,6,19]))
print(smallHash([7,6,19]))

# assignmen3
"""func get 2 math func and return the intercept point"""


def interceptPoint(m1, n1, m2, n2):
    if m1 != m2:
        x = (n2 - n1) / (m1 - m2)
        y = m1 * x + n1
        point = (x, y)
        return point
    else:
        return "none"


print(interceptPoint(5,4,5,9))
print(interceptPoint(2,4,5,-2))
print(interceptPoint(3,11,5,1))
print(interceptPoint(5,4,5,4))


# assignmen4
"""func get num and sum all the prime number"""



def factorSum(Num):
    primeSum = 0
    if Num < 2:
        return "invalid value"

    def isPrime(y):
        for i in range(2, y):
            if y % i == 0:
                return False
        return True

    for x in range(2, Num):
        if Num % x == 0 and isPrime(x):
            Num = Num / x
            primeSum = primeSum + x
    return primeSum


print(factorSum(60))

print(factorSum(81))
print(factorSum(221))

# assigment5
"""func get a string and check if all the brackets are close and return true else return false"""


def bracketsCheck(str):
    if str.count("(") == str.count(")"):
        if len(str) == 0:
            return True
        elif str[0] != '(':
            return bracketsCheck(str[1:])
        elif str[-1] != ')':
            return bracketsCheck(str[:-1])
        elif str[0] == '(' and str[-1] == ')':
            return bracketsCheck(str[1:-1])
        else:
            return False
    else:
        return False


print(bracketsCheck('()'))
print(bracketsCheck('())'))
print(bracketsCheck('())('))
print(bracketsCheck('(a))('))
print(bracketsCheck('a(bc{d)(8)'))
print(bracketsCheck('a(bc[]][)'))

# assignment6
"""func get num and print its binary val"""


def printBin(Num):
    Num = math.floor(Num)
    if Num <= 0:
        return 1
    if Num % 2 == 0:
        printBin(Num / 2)
        print("0", end="")
    if Num % 2 == 1:
        printBin(Num / 2)
        print("1", end="")


# assignment7
"""calculate the even factorial [1,n]"""


def evenFactorial(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return evenFactorial(n - 1) * n
    else:
        return evenFactorial(n - 1) * 1
