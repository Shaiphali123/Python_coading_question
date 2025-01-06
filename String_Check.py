input1 = "dataScienceproject"
input2 = input1.lower()
print(input2)

list1 = ['data', 'pull', 'datas', 'quote']
list2 = []

for i in list1:
    if i in input2:
        list2.append(i)

print(list2)