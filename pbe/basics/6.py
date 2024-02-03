'''
006

Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a user-
friendly format.
'''

start = int(input('With how many number of pizzas you started with: '))
eaten = int(input('how many sices of pizza you already eaten: '))

answer = start - eaten

print(f'Hellow my frield you are left with {answer} number of pizzas')

