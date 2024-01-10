def find_min_max(glist):
    glist = sorted(glist)
    print(glist[0])
    print(glist[-1])
    min = 0 
    max = 0
    for i in range(len(glist)-1):
            if glist[i] > glist[i+1]:
                min = glist[i]
            elif glist[i] < glist[i+1]:
                max = glist[i+1]
    print("Minimum number is: " + str(min))
    print("Maximum number is: " + str(max))

list1 = [2, 3, 4, 1, 9]
find_min_max(list1)