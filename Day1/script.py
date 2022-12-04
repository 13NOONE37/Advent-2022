text = open('input.txt','r').readlines()

totalCalories = []
elvCalories = []
for line in text:
    if line=='\n':
        totalCalories.append(sum(elvCalories))
        elvCalories=[]
    else:
        elvCalories.append(int(line))
totalCalories.append(sum(elvCalories))
elvCalories=[]

#first task
print(max(totalCalories))

#second task
print(sum(sorted(totalCalories,reverse=True)[:3]))