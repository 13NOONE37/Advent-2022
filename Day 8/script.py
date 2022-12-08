with open('input.txt','r') as file_input:
    lines = file_input.readlines()
    index = len(lines)
    visible=0

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

    print(f"Visible: {visible}")