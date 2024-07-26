# https://codeforces.com/problemset/problem/80/A



# a,b = map(int,input().split())


# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# pri= [i for i in range(2,20) if prime(i)]

# if not b in pri:
#     print('NO')
# else:
#     index_a = pri.index(a)
#     index_b = pri.index(b)
#     if index_a + 1 == index_b:
#         print('YES')
#     else:
#         print('NO')


# index_a = pri.index(a)

# if a not in pri:
#     print('NO')

# elif index_a + 1 == pri.index(b):
#     print('YES')
# else:
#     print('NO')



a,b = map(int,input().split())


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if (prime(a) == True) and (prime(b) == True):
    pr = []

    for i in range(a,b+1):
        if prime(i):
            pr.append(i)

    if pr.index(b) == pr.index(a) + 1:
        print('YES')
    else:
        print('NO')

else:
    print('NO')

# pri= []

# for i in range(2,51):
#     if prime(i):
#         pri.append(i)


# index = pri.index(a)

# if pri[index + 1] == b:
#     print('YES')
# else:
#     print('NO')