my_list=[1,2,2,4,4,6,8,10,13,22,35,52,83]
list=[]
for i in my_list:
    if i>=10:
        list.append(i)
print(list)
n=int(input())
list_1 =[]
for i in my_list:
    if i>=n:
        list_1.append(i)
print(list_1)
