n = input()
stat_list = []  # original input list

for i in range(int(n)):
    stat_list.append(input())   # Taking input from user
    stat_list[i] = stat_list[i].split(':')    # separating keyword from values
    for j in range(1, len(stat_list[i])):
        stat_list[i][j] = stat_list[i][j].split(',')    # separating different values of inner dictionary
        for k in range(len(stat_list[i][j])):
            stat_list[i][j][k] = stat_list[i][j][k].split('-')  # separating keywords of inner dictionary from values

inner_dic_list = []

for i in range(int(n)):
    for j in range(1, len(stat_list[i])):
        dic = {}
        for k in range(len(stat_list[i][j])):
            dic[stat_list[i][j][k][0]] = stat_list[i][j][k][1]
        inner_dic_list.append(dic)   # converting to list of inner dictionary values

final_dic = {}
for i in range(int(n)):
    final_dic[stat_list[i][0]] = inner_dic_list[i]  # assigning inner dictionaries to keyword of outer dictionary

print(final_dic)

list_coll = []  # list without outer dictionary keywords
for i in range(int(n)):
    for j in range(1, len(stat_list[i])):
        for k in range(len(stat_list[i][j])):
            list_coll.append(list(stat_list[i][j][k]))    # creating a list of lists with name and score pairs

list_coll.sort()

x = list_coll[0][0]
sum_x = 0
list_x = []
prev_x = 0

for i in range(len(list_coll)):
    list_temp = []
    if x == list_coll[i][0]:
        sum_x = sum_x + int(list_coll[i][1])
        list_temp = [x, sum_x]
        if prev_x == x:
            list_x.pop()   # to delete repetitions
            list_x.append(list_temp)   # to attach list with final score
        else:
            list_x.append(list_temp)
        prev_x = x
    else:
        sum_x = int(list_coll[i][1])
        x = list_coll[i][0]
        prev_x = x
        list_temp = [x, sum_x]
        list_x.append(list_temp)

list_tuple = []
for i in range(len(list_x)):     # converting final list with added scores and sorted names into a list of tuples
    list_tuple.append(tuple(list_x[i]))

print(list_tuple)



# 3
# match1:p1-9,p2-38
# match2:p3-19,P1-49
# m3:p3-1,p4-6,p1-91
