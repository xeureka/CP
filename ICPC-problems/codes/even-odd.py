

length = int(input())
arr = list(map(int,input().split()))

odd = [i for i in arr if i % 2 !=0]
even = [i for i in arr if i % 2 ==0]

print(f'{sum(odd)} <=> {sum(even)}')