lines = open('input.txt','r').readlines()

def getSignScore(sign):
    if sign=='X':
        return 1
    if sign=='Y':
        return 2
    if sign=='Z':
        return 3


def isWinning(sign1, sign2):
    temp1='ABC'
    temp2='XYZ'

    if temp1.index(sign1) == temp2.index(sign2):
        return 3
    if (
       (sign2=='X' and sign1=='C') or 
       (sign2=='Y' and sign1=='A') or 
       (sign2=='Z' and sign1=='B')):
        return 6

    return 0

def decideWin(sign1, sign2):
    temp1='ABC'
    temp2='XYZ'
    index1=temp1.index(sign1)

    if sign2=='X':
        #loss
        return 0 +getSignScore(temp2[(index1-1)%3]) 
    if sign2=='Y':
        #draw
        return 3+getSignScore(temp2[index1])
    if sign2=='Z':
         return 6+getSignScore(temp2[(index1+1)%3]) 
        

ammount=0
for line in lines:
    opponentSign=line[0]
    ourSign=line[2]
    #part1
    # ammount+=getSignScore(ourSign)+isWinning(opponentSign,ourSign)

    #part2
    ammount+=decideWin(opponentSign,ourSign)
print(f"Total score🎆🎆: {ammount}")

