# Link of problem
#https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/toy-box-5044b3ed/
#

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
P = []
B = []
finalp = []
finalb = []
N, M = input().split(' ')
N = int(N)
M = int(M)


for i in range(0,N):
    Inp = input()
    a, b = Inp.split(' ')
    P.append(int(a))
    B.append(int(b))
#    if (box[B[i]] is None)  or box[B[i]] < P[i]:
#        box[B[i]] = P[i]

for x in range(0,len(B)):
    #ind = B.index(x)
    temp = B[x]
    if temp in finalb:
        ind2 = finalb.index(temp)
        if P[x] > finalp[ind2]:
            finalp[ind2]=P[x]
    else:
        finalb.append(B[x])
        finalp.append(P[x])

print(sum(finalp))
