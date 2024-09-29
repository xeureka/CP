# odd index from list one
# even index from even list

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd = [l1[i] for i in range(len(l1)) if i % 2 != 0]
even = [l2[i] for i in range(len(l2)) if i % 2 ==0]

print('Element at odd-iindex posistion from list one')
print(odd)


print('Element at even-index positions from list two')
print(even)


