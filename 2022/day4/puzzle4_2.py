#Advent of Code Day 4 part 2
#4th December, 2022

def find_overlaps(pairs):
  overlaps = []
  for pair in pairs:
    a, b = pair.split(',')
    start_a, end_a = [int(x) for x in a.split('-')]
    start_b, end_b = [int(x) for x in b.split('-')]
    if (start_a <= end_b and start_a >= start_b) or (start_b <= end_a and start_b >= start_a):
      overlaps.append(pair)
  return overlaps

output =  0 
pairs = []

with open('puzzle4.txt') as f:
     for line in f:
        pairs.append(line.rstrip('\n'))
        if not line:
            break

overlaps = find_overlaps(pairs)
print(len(overlaps))


