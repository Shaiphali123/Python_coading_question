string1 = "aaddbbssggejjiiffffffkq"
string2 = ""
count = 1


for i in range(1,len(string1)+1):

    if i < len(string1) and string1[i] == string1[i-1]:
        count+= 1

    else:
        string2 +=string1[i-1] +(str(count) if count > 1 else"")
        count = 1

print(string2)


