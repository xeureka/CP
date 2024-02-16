# Challenge: write a function merge_arrays(), that takes two lists of integers as inputs,
#   combines them, removes duplicates, sorts the combined list and returns it


def merge_arrays(lst1,lst2):
    com_list = lst1 + lst2
    com_list = set(com_list)
    com_list = list(com_list)
    com_list.sort()
    return com_list


    
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))


print(merge_arrays(lst1,lst2))