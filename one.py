def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i
       print theSum, i
   return theSum

print(sumOfN(10))
'''
1 1
3 2
6 3
10 4
15 5
21 6
28 7
36 8
45 9
55 10
55
'''
