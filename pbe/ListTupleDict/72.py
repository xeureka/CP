'''
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.


'''

subjects = ['math','physics','chemistry','history','geography','english']

res = input('Enter the subject you dont like from the above lists: ').lower()

subjects.remove(res)

print(subjects)