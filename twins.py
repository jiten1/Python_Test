twin1 = input("Enter first name:")
twin2 = input("Enter second name:")
count1 = 0
count2 = 0
occupied = []
if (sorted(twin1) == sorted(twin2)):
    print("True")
    while count1 != len(twin1):
        if twin1[count1] == twin2[count2]:
            if count2 not in occupied:
                print(f'({count1},{count2})',end ="")
                occupied.append(count2) 
                count1 += 1
                count2 = 0
            elif count2 != len(twin2):
                count2 +=1
        elif count2 != len(twin2):
                count2 +=1
else:
    print("False")
