A = []
m = len(A)
for m in range(0,15):
    x=int(input())
    A.append(x)




print('Исходный массив A')
print(A)

s = 0
k=0
for i in range(len(A)):
    if A[i]>12:
        s += A[i]
        k +=1
print('s =', s)
print('k =', k)
