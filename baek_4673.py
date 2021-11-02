def solution1(n):
    sum = 0
    while n>0:
        sum = sum + (n % 10)
        n = (n-(n%10))/10
    return int(sum)

def d(n) :
    return n + solution1(n)

k=[]
for i in range(1,10001):
    k.append(d(i))

print(sorted(k))
k = sorted(k)

number = list(range(1,10001))

self_num = [x for x in number if x not in k]

for i in self_num:
    print(i)
