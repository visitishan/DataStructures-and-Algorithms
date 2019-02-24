# Link of problem
# https://www.hackerearth.com/problem/algorithm/palindromes-3-7dbdca4b/
#
# Partially Correct, not passed all test cases.

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
count = 0
N, Q = input().split(' ')
N = int(N)
Q = int(Q)
S = []
Akacount = 0


for i in range(N):
    temp = input()
    S.append(temp)

for j in range(0,Q):
    OP = input()
    OP = OP.split(' ')
    if OP[0] == '1':
        A= int(OP[1]) ^ Akacount
        B= int(OP[2]) ^ Akacount
        if A == 2:
            S[0] = S[0]+S[A]
            S[A] = '\0'
        else:
            #S[A-1] = S[A-1]+S[B-1]
            S[0] = S[0]+S[B-1]
            S[B-1] = '\0'
        #print(A)
        #print(B)
        #print(S)
    elif OP[0] == '2':
        new = S[int(OP[1])-1]
        newstr = new[0:int(OP[2])-1] + str(OP[3]) + new[int(OP[2])-1:]
        S[int(OP[1])-1] = newstr
    
    count = 0
    for i in range(0,N):
        reversestring = "".join(reversed(S[i])) 
        if S[i]==reversestring and S[i]!='\0':
            count = count + 1
    
#    Akacount = Akacount+count
    Akacount = count
    print(count)
        
