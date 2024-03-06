# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true



# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'


try:
    a = int(input())
    b = int(input())
    result = a / b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(result)