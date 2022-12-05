lines = open('input.txt','r').readlines()

def getCharacterValue(character):
    if character.isupper():
        return ord(character)-38
    else:
        return ord(character)-96

ammount=0

characters=""
#part1
# for line in lines:
#     part1 = line[:len(line)//2]
#     part2 = line[len(line)//2:]
#     for x in part1:
#         if part2.count(x)>0:
#             characters+=(x)
#             break

# part2
for i in range(0,len(lines),+3):
    part1 = lines[i]
    part2 = lines[i+1]
    part3 = lines[i+2]

    for x in part1:
        if part2.count(x)>0 and part3.count(x)>0:
            characters+=(x)
            break


for x in characters:
    ammount+=getCharacterValue(x)
    
print(f"Result: {ammount}")


