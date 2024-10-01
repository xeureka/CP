# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = int(len(sample_list) / 2)

start = 0
end = len(sample_list)

for i in range(3):
    ind = slice(start,end)

    lst = sample_list[ind]
    print('Chunk' ,i,lst)
    print('rev' , lst[::-1])

    start = end
    end += len(sample_list)

    