#Palindrome problem February circuits
#Problem Link - https://www.hackerearth.com/problem/algorithm/palindromes-3-7dbdca4b/
#

# Write your code here
count = 0
N, Q = input().split(' ')
N = int(N)
Q = int(Q)
S = []

for i in range(N):
    temp = input()
    S.append(temp)

for j in range(0,Q):
    OP = input().split(' ')
    A= count ^ int(OP[1])
    B= count ^ int(OP[2])
    A=A-1
    B=B-1
    if OP[0] == '1':
        S[A] = S[A]+S[B]
        S[B] = '\0'
    elif OP[0] == '2':
        if B == len(S[A]):
            S[A] = S[A] + str(OP[3])
        else :
            new = S[A]
            S[A] = new[0:B] + str(OP[3]) + new[B:]

    count = 0
    for i in range(0,N):
        reversestring = "".join(reversed(S[i])) 
        if S[i]==reversestring and S[i]!='\0':
            count = count + 1
    
    print(count)
