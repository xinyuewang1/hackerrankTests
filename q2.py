def solution(S):
    stack = []
    for x in S:
        print(stack)
        if x.isdigit():
            stack.append(int(x))
        elif x == "+":
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                if a+b > 4095:
                    print(a, "+", b, " lead to a stack overflow.")
                    return -1
                stack.append(a+b)
                # print(stack)
            else:
                print("Not enough element on stack to perform", a, "+", b)
                return -1
        elif x == "*":
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                if a*b > 4095:
                    print(a, "*", b, " lead to a stack overflow.")
                    return -1
                stack.append(a * b)
            else:
                print("Not enough element on stack to perform", a, "*", b)
                return -1
    return stack.pop()

print(solution("13+62*7+*"))
print(solution("11++"))