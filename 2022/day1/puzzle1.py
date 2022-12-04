#Advent of Code Day 1
#3rd December, 2022
#Program to find the maximum sum of consecutive digits before a line break/empty line

digit = []
sum = 0
answer = []

with open('puzzle1.txt') as f:
     for line in f:
        digit.append(line.rstrip('\n'))
        if line=='':
            digit.append(sum)
            sum = 0
        if not line:
            break

for x in digit:
    if x != '':
        sum += int(x)
    else:
        answer.append(sum)
        sum = 0


print("The highest sum is:",max(answer))

#Snippet of code to find the max 3 values of the sums
answer.sort(reverse=True) 
second_answer = answer[0]+answer[1]+ answer[2]
print(second_answer)