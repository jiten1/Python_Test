a = [1,2,3,2,5,1,2,4,6,2,7,8,6]
count1 = 0
count2 = 0
e = 0
for i in a:
    for j in a[(count1+1) : len(a)]:
        if i == j:
            d = count2-count1
            if d > e:
                e = d
        count2+=1
    count1+=1
    count2 = count1+1
print (e)