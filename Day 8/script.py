with open('input.txt','r') as file_input:
    lines = file_input.readlines()
    index = len(lines)
    visible=0
    highestScore=1
    
    #part1
    for x in range(0,index):
        for y in range(0,index):
            tree = int(lines[y][x])
            leftValues=[]
            rightValues=[]
            topValues=[]
            bottomValues=[]

            #top
            for i in range(y,0,-1):
                if int(lines[i-1][x]) >= tree:
                    topValues.append(int(lines[i-1][x]))
            #bottom
            for i in range(y+1, index):
                if int(lines[i][x]) >= tree:
                    bottomValues.append(int(lines[i][x]))
            #left
            for i in range(x-1,-1,-1):
                if int(lines[y][i]) >= tree:
                    leftValues.append(int(lines[y][i]))
            #right
            for i in range(x+1, index):
                if int(lines[y][i]) >= tree:
                    rightValues.append(int(lines[y][i]))
           
            if len(leftValues)==0 or len(rightValues)==0 or len(topValues)==0 or len(bottomValues)==0:
               visible+=1

    #part2
    for x in range(0,index):
        for y in range(0,index):
            tree = int(lines[y][x])
            leftValues=[]
            rightValues=[]
            topValues=[]
            bottomValues=[]

            #top
            for i in range(y,0,-1):
                currentTree = int(lines[i-1][x])
                topValues.append(currentTree)
                if  currentTree>=tree:
                    break      
            #bottom
            for i in range(y+1, index):
                currentTree = int(lines[i][x])
                bottomValues.append(currentTree)
                if  currentTree>=tree:
                    break  
            #left
            for i in range(x-1,-1,-1):
                currentTree = int(lines[y][i])
                leftValues.append(currentTree)
                if  currentTree>=tree:
                    break   
            #right
            for i in range(x+1, index):
                currentTree = int(lines[y][i])
                rightValues.append(currentTree)
                if  currentTree>=tree:
                    break   
               
            scenicScore = len(topValues)*len(bottomValues)*len(leftValues)*len(rightValues)
            if scenicScore>highestScore:
                highestScore=scenicScore
            

          
    print(f"Visible: {visible}")
    print(f"HighestScore: {highestScore}")

