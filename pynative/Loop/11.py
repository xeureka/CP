# Exercise 11: Write a program to display all prime numbers within a range


start = int(input())
end = int(input())

ans = []

for i in range(start,end+1):
    for j in range(2,start):
        if i % j == 0:
            break
    else:
        ans.append(i)

print(ans)