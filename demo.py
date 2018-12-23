def solution(A, B):
    # write your code in Python 3.6
    A, B = str(A), str(B)
    ans = ""
    # error check
    if len(A) + len(B) >= 9:
        return -1
    for i in range(min(len(A), len(B))):
        # print(A[i])
        ans += A[i]
        ans += B[i]
    if len(A) > len(B):
        ans += A[len(B):]
    elif len(A) < len(B):
        ans += B[len(A):]
    return int(ans)

print(solution(1234,678))
print(solution(111111,222))