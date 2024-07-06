# https://codeforces.com/problemset/problem/1716/A

for i in range(int(input())):
    num = int(input())

    def parity(n):
        if num % 2 ==0:
            return True
        else:
            return False

    if num == 1 or num ==-1:
        print(2)
    else:
        if parity(num) == True and (num % 3 ==0):
            print(num /3)
        else:
            if (num % 3 == 1):
                print((num % 3) +1)
  