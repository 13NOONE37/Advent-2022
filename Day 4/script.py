def get_difference(numbers):
    high = max(numbers)
    low = min(numbers)
    return high - low

amount = 0
#part1
# with open('test.txt', 'r') as input_file:
#     for line in input_file:
#         line = line.split(',')
#         range1 = list(map(int, line[0].split('-')))
#         range2 = list(map(int, line[1].split('-')))
#         if get_difference(range1) > get_difference(range2):
#             # First range is bigger
#             if range2[0] >= range1[0] and range2[1] <= range1[1]:
#                 amount += 1
#         elif get_difference(range2) > get_difference(range1):
#             # Second range is bigger
#             if range1[0] >= range2[0] and range1[1] <= range2[1]:
#                 amount += 1
#         elif range1 == range2:
#             # Ranges are the same
#             amount += 1

#part2
def find_common(range1,range2):
    for i in range(range1[0],range1[1]+1):
            for j in range(range2[0],range2[1]+1):
                if i==j:
                    return 1
    return 0
                    
with open('input.txt', 'r') as input_file:
    for line in input_file:
        line = line.split(',')
        range1 = list(map(int, line[0].split('-')))
        range2 = list(map(int, line[1].split('-')))
        
        amount+=find_common(range1,range2)
            

print(f"Result: {amount}")
