# def target_sum(list1,target):
#     seen = []
#     list2 = []
#
#     for i in list1:
#         diff = target - i
#         if diff in seen:
#             list2.append([i,diff])
#
#         seen.append(i)
#
#     return list2
#
# output = target_sum([10,23,9,34,19,24],33)
# print(output)


list1 = [10,23,9,34,19,24]
target = 33

seen = {}
list3 = []

for i in range(len(list1)):
    diff = target - list1[i]
    if diff in seen:
        list3.append([i, seen[diff]])

    seen[list1[i]] = i

print(seen)
print(list3)


for i in range(len(list1)):
    diff = target - i
    if diff in list3:
        list3.append([i,diff])

print(list3)








#i/p :list1 = [10,23,9,34,19,24] target = 33
#0/p : [[10,23][9,24]]