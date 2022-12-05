#Advent of Code Day 3 part 2
#4th December, 2022

output = 0

import itertools
with open('puzzle3.txt') as f:
    for group in itertools.zip_longest(*[f]*3):
        s1 = set(group[0].rstrip('\n'))
        s2 = set(group[1])
        s3 = set(group[2])
        char = s1 & s2 & s3
        print(char)
        
            
        iterator = iter(char)
        item = next(iterator, None)
      
        if (ord(item) > 96):
            output += ord(item) - 96
        else:
            # print("actual", item,  ord(item))
            output+= ord(item) - 38 #eg: A = 41 - 38 = 27
          
     
        
print(output)