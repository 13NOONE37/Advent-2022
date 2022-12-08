import re
with open('input.txt','r') as file_input:
    lines = file_input.readlines()
    
    path=''
    dirs={}

    for i in range(0,len(lines)):
        line = lines[i]
        line = line.split(' ')
        line[-1]= line[-1].split('\n')[0]
        
        
        if line[1]=='cd':
            #monitor path
            match line[2]:
                case '/':
                    path='/'
                    # break
                case '..':
                    keys = path.split('/')[:-2]
                    path='/'.join(keys)+'/'
                    # break
                case other:
                    name = line[-1]
                    path+=name+'/'
                    # break
        elif line[0].isnumeric():
            
            dirs[path] = dirs.get(path,[])+[' '.join(line)]
            

    amount=0
    for dir in dirs.keys():
        tempSum=[]
        for key, value in dirs.items():
            # print(f"Dir: {dir}, Key: {key}, Value: {value}")
            if key.startswith(dir):
                temp = value
                temp = [inner.split(' ') for inner in temp]
                temp = [int(inner[0]) for inner in temp]
                tempSum+=temp
            
        total = sum(tempSum)
        if total < 100000:
            amount+=total

        
     

    print(f"Total: {amount} shuld be 1648397")