def isDiffrent(prev):
    for char in prev:
        if prev.count(char)>1:
            return False
    return True

with open('input.txt','r') as file_input:
    line = file_input.readline()
    result=0
    
    #part1
    # characterCount=4

    #part2
    characterCount=14

    for x in range(0,len(line)):
        prev=[]
        for y in range(x,min(x+characterCount,len(line))):
            prev.append(line[y])

        if isDiffrent(prev):
            result=x+characterCount
            break
    print(f"Result: {result}")