#Advent of Code Day 3 part 1 
#4th December, 2022


output =  0 

with open('puzzle3.txt') as f:
     for line in f:
      
        linelen = len(line.rstrip('\n'))
        half = int(linelen/2)
     
        comp1 = set(line[0:half])
        comp2 = set(line[half:])
        char = comp1 & comp2
      
        iterator = iter(char)
        item = next(iterator, None)
      
        if (ord(item) > 96):
            output += ord(item) - 96
            print("small", ord(item)- 96)
        else:
            print("actual", item,  ord(item))
            output+= ord(item) - 38 #eg: A = 41 - 38 = 27
          
        if not line:
            break
        
print(output)
