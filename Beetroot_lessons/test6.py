a_list = []
for i in range(18):
    if i % 2 == 0:
        continue
    a_list.append(i)

print(sum(a_list) // 27)
print(a_list)
