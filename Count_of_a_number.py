""" write a function to count the Number from the Given list or string
For Example : list1 = [1,2,2,3,4,5,6,7,7,8,8,1,2,3,4,5,5,6,7,8,2,3]
o/p: {1:4, 2:4}
"""

def count_Number(string1):
    dict1 = {}

    for i in string1:
        if i in dict1:
            dict1[i] +=1

        else:
            dict1[i] = 1

    filtered_dict = {key:value for key,value in dict1.items() if value > 1}

    return filtered_dict

string1 = [1,2,3,4,5,6,6,2,3,4,5,6,6,7,7,8,89,45,3,4,5,66,7,7,7]

Find_count_string = count_Number(string1)
print(Find_count_string)