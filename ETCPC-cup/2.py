
n = int(input())
locations = set()
for i in range(n):
    names = input()
    list_ = names.split(" ") 
    locations.add(list_[5])

    if len(locations) > 1:
        print(list_[0]+ " did it!")
        exit()

    if list_[6] == "alone":
        print(list_[0] + " did it!")
        exit()

print("It was me!")

    