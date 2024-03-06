

# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'


for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)
