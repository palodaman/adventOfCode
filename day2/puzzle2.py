#Advent of Code Day2
#3rd December, 2022
#Program to find the output of a game of rock paper scissor

#Rock: 1, Paper:2, Scissor:3
# A B C 
# 1 2 3
# X Y Z
# Win: 6, Draw: 3, Lose:0
d = {"A X": 4, "A Y":8, "A Z":3, 
     "B X": 1, "B Y":5, "B Z":9,
     "C X": 7, "C Y":2, "C Z":6}

points = 0

with open('puzzle2.txt') as f:
     for line in f:
        if line.rstrip('\n') in d:
            points+= d[line.rstrip('\n')]
        if not line:
            break
        
#X: Lose Y: Draw Z: Win
d2 = {"A X": 3, "A Y":4, "A Z":8, 
     "B X": 1, "B Y":5, "B Z":9,
     "C X": 2, "C Y":6, "C Z":7}

points2= 0
with open('puzzle2.txt') as f:
    for line in f:
        if line.rstrip('\n') in d2:
            points2+= d2[line.rstrip('\n')]
            print(line)
        if not line:
            break
print(points)
print(points2)
     