
# https://codeforces.com/gym/542051/problem/A

for i in range(int(input())):
    num = int(input())
    val = input()

    ans = list(val)

    while True:
            try:
                if (ans[0] == '1' and ans[-1] == '0') or (ans[0] == '0' and ans[-1] == '1'):

                    ans.pop(0)
                    ans.pop(-1)
                else:
                    break
            except:
                break
                

    print(len(ans))
