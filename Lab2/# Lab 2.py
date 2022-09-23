# Lab 2 Darby Kirkland

# Part 1: Take the following list and multiply all list items together.
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def multiplyList(part1list):

    result = 1
    for x in part1list:
        result = result * x
    return result
 
 
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
print('Part 1 - The product is of all numbers in the list: ' + str(multiplyList(part1)))

# Part 2: Take the following list and add all list items together.
# [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

def addList(part2list):

    result = 1
    for x in part2list:
        result = result + x
    return result
 
 
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
print('Part 2 - The sum of all numbers in the list: ' + str(addList(part2)))

#Part 3: Take the following list and only add together those list items which are even. 
# You can use the following snippet of code to see if a number is even or odd. 
# The % operation is called Modulo and is used to find the remainder after division of one number by another. 
# We divide by 2 and look at the remainder; if there is no remainder the number is even, if there is a remainder the number is odd.
# isEven = part3 % 2 == 0
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result = 0
for item in part3:
    if not item%2:
        result += item
print('Part 3 - The sum of all even numbers in the list: ' + str(result))





