import re

with open('input.txt','r') as input_file:
    lines = input_file.readlines()
    instructionsIndex=1
    stacksLines=[]
    stacks=[]
    stacksIndexes=[]
    
    #Here we get the stacks
    for line in lines:
        if line=='\n':
            break
        stacksLines.append(line)
        instructionsIndex+=1
    for x in stacksLines[-1]:
        if x.isnumeric():
            stacksIndexes.append(stacksLines[-1].index(x))
    for x in stacksIndexes:
        temp=[]
        for line in stacksLines:
            char = line[x]
            if char.isnumeric()==False and char!=' ':
                temp.append(char)
        stacks.append(temp)
    stacks=[list(reversed(inner)) for inner in stacks]
    
    #Here we get instructions
    for line in lines[instructionsIndex:]:
        procedure=re.findall(r'\d+',line)#regullar expression says one digit or more
        procedure=list(map(int,procedure))
        
        fromIndex=procedure[1]-1
        toIndex=procedure[2]-1
        count=procedure[0]
        #part1
        # for i in range(-1,-(count+1), -1):
        #     stacks[toIndex].append(stacks[fromIndex][-1])
        #     del(stacks[fromIndex][-1])
            
        #part2
        temp = stacks[fromIndex][-(count):]
        del(stacks[fromIndex][-(count):])
        stacks[toIndex]+=temp
          
    
    result=''
    for stack in stacks:

        result+=stack[-1]

    
    print(f"Result: {result}")
