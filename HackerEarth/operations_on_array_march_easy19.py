#Operations on array - March Easy 2019
#Problem link - https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/operations-on-an-array-2187f48a/
#Partially working

# Write your code here
number = input()
a = map(int, input().split())
 
a = list(a)
 
avg = sum(a)/len(a)
diff = 0
maxd = max(a)
val = 0
count = 0
 
for i in range(len(a)):
    if((a[i] < avg)):
        diff = avg - a[i];
 
    if(diff < maxd):
        maxd = diff
        val = a[i]
 
for j in range(len(a)):
    diff1 = abs(val - a[i])
    count = count + diff
 
print(int(count))
