#Palindromes problem in March Easy 2019
#problem link - https://www.hackerearth.com/problem/algorithm/permutations-3-5d18252f/
#

# Write your code here
t = int(input())

def transf(a):
    x = len(a)
    temp = list(a)
    for j in range(0,x):
        v=temp[j]
        v=v-1
        a[j] = temp[v]
    return a
    
while(t):
    t = t-1
    
    n = int(input())
    a = map(int, input().split())
    a = list(a)
    b = list(a)
    b.sort()
    counter = 0
    
    while(a!=b):
        counter = counter+1
        a = transf(a)
        if (counter>20):
            counter = -1    
            break
    
    print(counter)
