

num = int(input())
sum1 = 0

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(2, num):
    sum1 = n1 + n2

    print(sum1)

    tem = n1
    n1 = n2
    n2 = sum1